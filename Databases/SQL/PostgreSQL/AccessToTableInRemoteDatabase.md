# PostgreSQL

## postgres_fdw
You can access data in a table on a remote database server with the postgres_fdw extension. 

### To use postgres_fdw to access a remote database server

1. Install the postgres_fdw extension.


```sh
CREATE EXTENSION postgres_fdw;
```

2. Create a foreign data server using CREATE SERVER.

```sh
CREATE SERVER foreign_server
FOREIGN DATA WRAPPER postgres_fdw
OPTIONS (host 'xxx.xx.xxx.xx', port '5432', dbname 'foreign_db'); 
```

3. Create a user mapping to identify the role to be used on the remote server.

```sh
CREATE USER MAPPING FOR local_user
SERVER foreign_server
OPTIONS (user 'foreign_user', password 'password');
```

4. Create a table that maps to the table on the remote server.

```sh
CREATE FOREIGN TABLE foreign_table (
        id integer NOT NULL,
        data text)
SERVER foreign_server
OPTIONS (schema_name 'some_schema', table_name 'some_table');
```

5. Test foreign table
```sh
SELECT * FROM foreign_table;
```

### DROP SERVER — remove a foreign server descriptor
```sh
DROP SERVER [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]
```