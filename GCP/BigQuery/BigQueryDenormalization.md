# Denormalization

Data warehouse schemas have historically used the following models:

- **Star schema:** This is a denormalized model, where a fact table collects metrics such as order amount, discount, and quantity, along with a group of keys. These keys belong to dimension tables such as customer, supplier, region, and so on. Graphically, the model resembles a star, with the fact table in the center surrounded by dimension tables.
- **Snowflake schema:** This is similar to the star schema, but with its dimension tables normalized, which gives the schema the appearance of a unique snowflake.

BigQuery supports both star and snowflake schemas, but its native schema representation is neither of those two. It uses nested and repeated fields instead for a more natural representation of the data.

Changing your schema to use nested and repeated fields is an excellent evolutionary choice. It reduces the number of joins required for your queries, and it aligns your schema with the BigQuery internal data representation. Internally, BigQuery organizes data using the Dremel model and stores it in a columnar storage format called Capacitor.

## Specify nested and repeated columns in table schemas

### Define nested and repeated columns
To create a column with nested data, set the data type of the column to RECORD in the schema. A RECORD can be accessed as a STRUCT type in GoogleSQL. A STRUCT is a container of ordered fields.

To create a column with repeated data, set the mode of the column to REPEATED in the schema. A repeated field can be accessed as an ARRAY type in GoogleSQL.

A RECORD column can have REPEATED mode, which is represented as an array of STRUCT types. Also, a field within a record can be repeated, which is represented as a STRUCT that contains an ARRAY. An array cannot contain another array directly.

Example schema:

The following example shows sample nested and repeated data. This table contains information about people. It consists of the following fields:

- id
- first_name
- last_name
- dob (date of birth)
- addresses (a nested and repeated field)
    - addresses.status (current or previous)
    - addresses.address
    - addresses.city
    - addresses.state
    - addresses.zip
    - addresses.numberOfYears (years at the address)

The JSON data file would look like the following:

```
{"id":"1","first_name":"John","last_name":"Doe","dob":"1968-01-22","addresses":[{"status":"current","address":"123 First Avenue","city":"Seattle","state":"WA","zip":"11111","numberOfYears":"1"},{"status":"previous","address":"456 Main Street","city":"Portland","state":"OR","zip":"22222","numberOfYears":"5"}]}
{"id":"2","first_name":"Jane","last_name":"Doe","dob":"1980-10-16","addresses":[{"status":"current","address":"789 Any Avenue","city":"New York","state":"NY","zip":"33333","numberOfYears":"2"},{"status":"previous","address":"321 Main Street","city":"Hoboken","state":"NJ","zip":"44444","numberOfYears":"3"}]}

```

The schema for this table looks like the following:

```
[
    {
        "name": "id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "first_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "last_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "dob",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "addresses",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "status",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "address",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "city",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "state",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "zip",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "numberOfYears",
                "type": "STRING",
                "mode": "NULLABLE"
            }
        ]
    }
]
```

Examples:

#### Insert data in nested columns in the example
```
INSERT INTO mydataset.mytable (id,
first_name,
last_name,
dob,
addresses) values ("1","Johnny","Dawn","1969-01-22",
    ARRAY<
      STRUCT<
        status STRING,
        address STRING,
        city STRING,
        state STRING,
        zip STRING,
        numberOfYears STRING>>
      [("current","123 First Avenue","Seattle","WA","11111","1")])
```

```
INSERT INTO mydataset.mytable (id,
first_name,
last_name,
dob,
addresses) values ("1","Johnny","Dawn","1969-01-22",[("current","123 First Avenue","Seattle","WA","11111","1")])
```

#### Query nested and repeated columns
The following example selects the first name, last name, and first address listed in the addresses field
```
SELECT
  first_name,
  last_name,
  addresses[offset(0)].address
FROM
  mydataset.mytable;
```

The result is the following:

```
+------------+-----------+------------------+
| first_name | last_name | address          |
+------------+-----------+------------------+
| John       | Doe       | 123 First Avenue |
| Jane       | Doe       | 789 Any Avenue   |
+------------+-----------+------------------+
```


The following example selects the first name, last name, address, and state for all addresses not located in New York:

```
SELECT
  first_name,
  last_name,
  a.address,
  a.state
FROM
  mydataset.mytable CROSS JOIN UNNEST(addresses) AS a
WHERE
  a.state != 'NY';
```

The result is the following:

```
+------------+-----------+------------------+-------+
| first_name | last_name | address          | state |
+------------+-----------+------------------+-------+
| John       | Doe       | 123 First Avenue | WA    |
| John       | Doe       | 456 Main Street  | OR    |
| Jane       | Doe       | 321 Main Street  | NJ    |
+------------+-----------+------------------+-------+
```

#### When to use nested and repeated columns
BigQuery performs best when your data is denormalized. Rather than preserving a relational schema such as a star or snowflake schema, denormalize your data and take advantage of nested and repeated columns. Nested and repeated columns can maintain relationships without the performance impact of preserving a relational (normalized) schema.

Suppose you have the following table mydataset.books:

```
+------------------+------------+-----------+
| title            | author_ids | num_pages |
+------------------+------------+-----------+
| Example Book One | [123, 789] | 487       |
| Example Book Two | [456]      | 89        |
+------------------+------------+-----------+
```


You also have the following table, mydataset.authors, with complete information for each author ID:

```
+-----------+-------------+---------------+
| author_id | author_name | date_of_birth |
+-----------+-------------+---------------+
| 123       | Alex        | 01-01-1960    |
| 456       | Rosario     | 01-01-1970    |
| 789       | Kim         | 01-01-1980    |
+-----------+-------------+---------------+
```

If the tables are large, it might be resource intensive to join them regularly. Depending on your situation, it might be beneficial to create a single table that contains all the information:

```
CREATE TABLE mydataset.denormalized_books(
  title STRING,
  authors ARRAY<STRUCT<id INT64, name STRING, date_of_birth STRING>>,
  num_pages INT64)
AS (
  SELECT
    title,
    ARRAY_AGG(STRUCT(author_id, author_name, date_of_birth)) AS authors,
    ANY_VALUE(num_pages)
  FROM
    mydataset.books,
    UNNEST(author_ids) id
  JOIN
    mydataset.authors
    ON
      id = author_id
  GROUP BY
    title
);
```

The resulting table looks like the following:

```
+------------------+-------------------------------+-----------+
| title            | authors                       | num_pages |
+------------------+-------------------------------+-----------+
| Example Book One | [{123, Alex, 01-01-1960},     | 487       |
|                  |  {789, Kim, 01-01-1980}]      |           |
| Example Book Two | [{456, Rosario, 01-01-1970}]  | 89        |
+------------------+-------------------------------+-----------+
```
