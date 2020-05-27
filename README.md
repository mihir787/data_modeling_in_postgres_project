# Postgres Data Modeling

## Summary
Sparkify, a music streaming startup, is looking to get an understanding of what its users are
listening to. The analytics team is tasked with looking at JSON activity logs in conjunction
with JSON song metadata to build a song play record for analysis. This project requires building
and transforming and loading a song play fact table with song, artist, user, and time dimensions.

## Running the Files
Initially the database and tables must be created before the ETL script can be run.
To create the database tables ensure postgres is installed locally and that a `studentdb` with
password `student` exists. Ensure you are in the project root directory. Run `python create_tables`.
Upon successful run a database called `Sparkify` should be created with all the appropriate tables.

After the tables are created the ETL script can be run to insert the data records:
`python etl.py`. Upon successful run all the data should be inserted and can be queried.

## Explanation of Files
- The `EDA.ipynb` notebook was used to investigate the raw data. This was used to understand datatypes and
constraints used in the DDL statements.
- The `data` directory contains the raw CSV data that is eventually loaded into the database.
- The `sql_queries.py` file has all the raw sql query strings that are interpolated with parameters
at runtime. This includes all the DDL statements and the insert statements used during load.
- The `create_tables.py` file runs all the CREATE statements required to create the database structure.
- The `etl.py` file run the transformations and load steps required to insert the data into the new tables.
