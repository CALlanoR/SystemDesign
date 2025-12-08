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
<<<<<<< HEAD


To validate:

SELECT
    fs.srvname AS server_name,
    fw.fdwname AS wrapper_name,
    fs.srvoptions AS connection_options
FROM pg_foreign_server fs
JOIN pg_foreign_data_wrapper fw ON fw.oid = fs.srvfdw
=======
>>>>>>> fb6ccd846296da2115ba1b63a384d328eb0f992e
```

3. Create a user mapping to identify the role to be used on the remote server.

```sh
CREATE USER MAPPING FOR local_user
SERVER foreign_server
OPTIONS (user 'foreign_user', password 'password');
<<<<<<< HEAD

to validate:

SELECT 
    umuser::regrole AS local_user,
    srvname AS server_name,
    umoptions AS options
FROM pg_user_mappings;
=======
>>>>>>> fb6ccd846296da2115ba1b63a384d328eb0f992e
```

4. Create a table that maps to the table on the remote server.

```sh
CREATE FOREIGN TABLE foreign_table (
        id integer NOT NULL,
        data text)
SERVER foreign_server
OPTIONS (schema_name 'some_schema', table_name 'some_table');
<<<<<<< HEAD

Example:

CREATE FOREIGN TABLE external_admin_center_api_tags (
	id int4 NOT NULL,
	"name" varchar(255) NOT NULL,
	create_date timestamp NOT NULL,
	update_date timestamp NOT NULL,
	public bool
)
SERVER admincenter_mirror
OPTIONS (schema_name 'admin_center_api', table_name 'tags');
=======
>>>>>>> fb6ccd846296da2115ba1b63a384d328eb0f992e
```

5. Test foreign table
```sh
SELECT * FROM foreign_table;
```

### DROP SERVER — remove a foreign server descriptor
```sh
DROP SERVER [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]
```