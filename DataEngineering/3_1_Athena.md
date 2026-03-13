# Athena
## Optimizing Athena queries by using buckets
When you work with large datasets that are spread out across multiple files, two major goals are to optimize query performance and to minimize cost. Cost for Athena is based on usage, which is the amount of data that is scanned, and prices vary based on your Region.

Three possible strategies that you can use to minimize your costs and improve performance are compressing data, bucketizing data, and partitioning data.
- **Compressing data:** Compress your data by using one of the open standards for file compression (such as Gzip or tar). Compression results in a smaller size for the dataset when it's stored in Amazon S3.

- The cardinality of your data also effects how you should optimize your queries. There are two options to optimize based upon high or low cardinality. These are:
    - **Bucketizing data:** For high cardinality with data, store records in distinct buckets (not to be confused with S3 buckets) based upon a shared value in a specific field. Consider bucketizing data as part of the preprocessing phase of your data pipeline. 
        - Putting data in separate buckets works when you have data that has a high degree of cardinality. Cardinality refers to the number of distinct records in a database. 
    - **Partitioning data:** You can also use partitions to improve performance and reduce cost. Partitioning is used with low-cardinality data, which means that fields have few unique or distinct values.
        - If you are interested in querying a field with low cardinality, which means that the field has few unique values, you would partition the data instead of using distinct buckets. In some cases, your data will be partitioned by another process. 


## Using Athena views
You might have noticed that Athena can create views. Creating and using views with data can help to simplify analysis because you can hide some of the complexity of queries from users.

Athena supports running only one SQL statement at a time, but you can use views to combine data from various tables. You can also use views to optimize query performance by experimenting with different ways to retrieve data and then saving the best query as a view.

# Commands
## Create table with csv
```sql
CREATE EXTERNAL TABLE IF NOT EXISTS taxidata.yellow (
    `vendor` string,
    `pickup` timestamp,
    `dropoff` timestamp,
    `count` int,
    `distance` int,
    `ratecode` string,
    `storeflag` string,
    `pulocid` string,
    `dolocid` string,
    `paytype` string,
    `fare` decimal,
    `extra` decimal,
    `mta_tax` decimal,
    `tip` decimal,
    `tolls` decimal,
    `surcharge` decimal,
    `total` decimal
  )
  ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
  WITH SERDEPROPERTIES (
    'serialization.format' = ',',
    'field.delim' = ','
  ) LOCATION 's3://aws-tc-largeobjects/CUR-TF-200-ACDSCI-1/Lab2/yellow/'
  TBLPROPERTIES ('has_encrypted_data'='false');
  ```

  ## Query
  ```sql
    SELECT COUNT (count) AS "Number of trips" ,
        SUM (total) AS "Total fares" ,
        pickup AS "Trip date"
    FROM yellow WHERE pickup
    BETWEEN TIMESTAMP '2017-01-01 00:00:00'
    AND TIMESTAMP '2017-02-01 00:00:01'
    GROUP BY pickup;
```

## To create a new table  partitioned for paytype = 1 (credit card transactions)
  ```sql
    CREATE TABLE taxidata.creditcard
    WITH (
    format = 'PARQUET'
    ) AS
    SELECT * 
    FROM "yellow"
    WHERE paytype = '1';
```

## Create view
  ```sql
    CREATE VIEW cctrips AS
    SELECT "sum"("fare") "CreditCardFares"
    FROM yellow
    WHERE ("paytype"='1');
```

## Create view that joins the data

```sql
    CREATE VIEW comparepay AS
    WITH
    cc AS
        (
            SELECT sum(fare) AS cctotal,
            vendor
            FROM yellow
            WHERE paytype = '1'
            GROUP BY paytype, vendor
        ),
    cs AS
        (
            SELECT sum(fare) AS cashtotal, vendor, paytype
            FROM yellow
            WHERE paytype = '2'
            GROUP BY paytype, vendor
        )
    SELECT cc.cctotal, cs.cashtotal
    FROM cc
    JOIN cs
    ON cc.vendor = cs.vendor;
```
