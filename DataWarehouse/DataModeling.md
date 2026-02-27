# Data Modeling
A data model defines how your data is:
- Structured
- Stored
- Related

## Database Model Options
1. Relational databases
2. Document Databases
3. Key-value Databases
4. Wide-Column Databases
5. Graph Databases

### Relational databases
A Relational Database Management System (RDBMS) is a structured data storage solution based on the relational model, where data is organized into predefined tables (relations) consisting of rows and columns. It ensures data integrity through a set of formal properties known as ACID (Atomicity, Consistency, Isolation, Durability) and uses SQL (Structured Query Language) as the standard interface for data manipulation and retrieval."

**Key Elements (The Building Blocks)**
- Tables & Schemas: Data is stored in relations with a strictly defined structure (schema).
- Keys (Primary & Foreign): These establish the "relationships" between tables, ensuring referential integrity across the dataset.
- Constraints: Rules (like NOT NULL, UNIQUE, or CHECK) that prevent invalid data from entering the system.
- Transactions: A sequence of operations treated as a single unit of work, ensuring the database remains in a consistent state even in the event of failure.

**When to Use Relational Databases**
You should opt for an RDBMS when:
- Data Integrity is Non-Negotiable: For financial systems, ERPs, or contract management where consistency is more important than raw write speed.
- Structured Data: When your data model is stable and you can define a clear schema upfront.
- Complex Querying: When you need to perform heavy joins and multi-dimensional analysis that SQL excels at.
- Relationships are Key: When the value of your data lies in how different entities (e.g., Users vs. Warehouse Orders) connect to each other.

Example (Users, posts and likes): 
<p align="center">
  <img src="./images/relationaltable1.png" width="600">
  <br/>
</p>

**Engine Best For...**
- PostgreSQL: The "Architect's Choice." Highly extensible, handles complex data types, and is perfect for deep engineering projects.
- MySQL: The web's favorite. Reliable, fast for read-heavy workloads, and widely supported by every cloud provider.
- Microsoft SQL Server: Enterprise environments heavily integrated with the .NET ecosystem and Azure.
- Oracle Database: Large-scale mission-critical applications requiring high-end security and massive data processing capabilities.
- Amazon Aurora: A cloud-native relational database (compatible with MySQL/Postgres) designed for high-performance and auto-scaling within AWS.

### Document Databases
A Document Database is a type of NoSQL database that stores data in flexible, JSON-like documents, allowing for schema evolution and easy integration with modern applications.

**Key Elements (The Building Blocks)**
- Documents: Data is stored in self-contained units (documents) that can have varying structures.
- Collections: Documents are grouped into collections, which are analogous to tables in relational databases.
- Flexible Schema: Unlike relational databases, document databases do not require a predefined schema, allowing for schema evolution and easy integration with modern applications.
- Query Language: Document databases use a query language that is specific to the database, allowing for flexible querying and data retrieval.

**When to Use Document Databases**
You should opt for a Document Database when:
- Your data is semi-structured or unstructured (e.g., JSON, XML, or text).
- You need a flexible schema that can evolve over time.
- You need to store and query complex, hierarchical data.
- You need to scale horizontally to handle large volumes of data.

Example (Users, posts and likes): 
<p align="center">
  <img src="./images/documentdb1.png" width="600">
  <br/>
</p>

**Engine Best For...**
- MongoDB: The "Developer's Favorite." Known for its flexibility and ease of use, making it a top choice for startups and fast-moving teams.
- Couchbase: The "Performance Powerhouse." Offers a unique hybrid model that combines the flexibility of document databases with the performance of key-value stores, making it ideal for high-performance applications.
- Amazon DocumentDB: The "Cloud-Native Choice." A fully managed document database service provided by AWS that is compatible with MongoDB, offering high scalability and availability.

### Key-Value Databases
A Key-Value Database is a simple yet powerful type of NoSQL database that stores data as a collection of key-value pairs, offering high performance and scalability for simple data retrieval operations.
- Key-value database is a complement of a another databases (Relational, Document, Graph)

**Key Elements (The Building Blocks)**
- Key-Value Pairs: Data is stored as a collection of key-value pairs, where each key is unique and maps to a specific value.
- Key: The key is a unique identifier for the value.
- Value: The value is the data that is stored in the database.

<p align="center">
  <img src="./images/keyvalue1.png" width="600">
  <br/>
</p>

**When to Use Key-Value Databases**
You should opt for a Key-Value Database when:
- Your data is simple and can be represented as key-value pairs.
- You need high performance and scalability for simple data retrieval operations.
- You need to store and query large volumes of data.
- You need to scale horizontally to handle large volumes of data.

**Engine Best For...**
- Redis: The "Speed Demon." Widely used as a cache and for real-time applications due to its in-memory architecture and support for various data structures.
- Memcached: The "Simplicity Champion." A high-performance, distributed memory caching system known for its simplicity and efficiency.
- DynamoDB: The "Scalability King." A fully managed key-value and document database service provided by AWS that offers high scalability and availability.

### Wide-Column Databases
A Wide-Column Store (also known as a Column-Family database) is a type of NoSQL database that organizes data into flexible, dynamic columns rather than fixed rows. Unlike traditional relational databases with rigid schemas, wide-column stores allow each row to have a different number of columns, making them highly effective for handling sparse data and massive, distributed datasets across multiple nodes.

**How a Query Works (The Logic)**
In a traditional Row-Oriented DB, if you want to find the "Email" of a user, the engine reads the entire row (Name, Address, Phone, Bio, etc.) from the disk to find that one field.

In a Wide-Column Store, data is stored in Column Families. When you query a specific column, the database skips the rest of the data and only reads the relevant column blocks. This drastically reduces I/O operations when you are dealing with billions of records and only need a few attributes.

**Key Elements**
- Column Family: A logical grouping of related columns (similar to a table, but more flexible).
- Row Key (Partition Key): The unique identifier for the row, which also determines how data is distributed across the cluster nodes.
- Clustering Key: Determines the physical sorting of data within the partition.
- Timestamp: Most engines (like Cassandra) store a version/timestamp for every cell to handle conflict resolution in distributed writes.

**When to Use Them (Architectural Decision)**
- Massive Scale: When you have petabytes of data that a single RDBMS cannot handle.
- High Write Throughput: Ideal for IoT, logging, or real-time tracking where you are writing thousands of events per second.
- Predictable Query Patterns: They are not great for "ad-hoc" queries (like SQL). You must design your table based on exactly how you plan to read the data.
- Sparse Data: When many records have null or different attributes, and you don't want to waste storage space.

**Engine Best For...**
- Apache Cassandra: The "Decentralized Champion." Built by Facebook to handle massive amounts of data across many commodity servers with no single point of failure.
- HBase: The "Hadoop Ecosystem Native." Integrates seamlessly with Hadoop's HDFS and MapReduce, making it a favorite for organizations already invested in the Hadoop stack.
- Google Bigtable: The "Foundation of Scale." The technology that powers Google's core services (Search, Analytics, Maps), known for its extreme scalability and performance.
- Redshift: The "Cloud Data Warehouse." A fully managed, petabyte-scale data warehouse service provided by AWS that is optimized for analytics and business intelligence.
- Snowflake: The "Cloud Data Platform." A cloud-native data warehouse that separates storage and compute, allowing for independent scaling and flexible pricing.
