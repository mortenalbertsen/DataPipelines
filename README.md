# DataPipelines

This repository holds source-code for a sample application, specifically extracting, converting and outputting a dataset. 

Technologies employed

- MySQL
- Python
- Apache AirFlow
- PonyORM

## Intended exercise
Setup and run an Airflow workflow, containing the following steps:
1. Ingest ("load") the data as-is from the provided csv file into a database table
2. Transform the loaded data (from step 1.) in the following way: 
*Use dbt to create a new table, or view, with the columns; “brewery_name”,
“beer_name”, and a new calculated column “avg_review_overall” (derived from
average “review_overall”)*



## Current progress

- Ingestion of raw data into database
  - Currently bothered by a unicode-parsing error when ingesting csv-file
- Transformation of data into desired format
  - Implementation not begun



## Current issues

- During import memory consumption increases monotonically to about ~4 GB. 



## Realize the following - and avoid frustration!

- The database used by AirFlow (in-memory or persisted) backs AirFlow itself, *but has nothing to do with the storage of the input to / output of the the data-tasks (if any) carried out by workflows managed by AirFlow*.
  - Hence, if one plans to setup workflows that persists data to a database, two separate / unrelated databases should come into play:
    - one for the AirFlow application / server (always needed) - the "airflow database"
      This database only holds data used to support AirFlow - data going in and out of workflows is *not* to be persisted in this database.
    - (optional, depending on need of workflow) another database for data-storage / manipulation, to be used by workflow tasks - the "data database". 
- AirFlow provides a `MySQLOperator`; that operator allows you to run sql-queries against the "data-database". I suggest one forgets about the eixstence of and/or does *not* use `MySQLOperator` to interact with the database, but rather use an ORM, for instance [PonyORM](https://docs.ponyorm.org), to interact with the database. 
- AirFlow really is two things: A) a python package, and B) a server that runs / monitor submitted workflows. 



## Dataset

Download beer-reviews dataset in local folder `data`

```bash
mkdir data/
cd data
curl https://s3.eu-west-2.amazonaws.com/tgtg-public-data/beer_reviews.csv.zip -o beer_reviews.csv.zip
unzip beer_reviews.csv.zip
```



### Learnings on dataset

- The following fields cannot be assumed to be present in dataset

  - `brewery_name`
  - `beer_abv`
  - `profile_name`

  

## Create database to back AirFlow application

Essential steps

1. Create database (i.e. named `AirFlowSupport`) to back AirFlow application

2. Create user (i.e. `AirFlowClient`, with password `sinceJyllandAlgebra812$$` ) for that database that Airflow will use when connecting to database

   1. Grant user all rights

3. Update `~/airflow/airflow.cfg`, specifically the `executor` and `sql_alchemy_conn` variables:

   ```
   # The executor class that airflow should use. Choices include
   # SequentialExecutor, LocalExecutor, CeleryExecutor, DaskExecutor, KubernetesExecutor
   executor = LocalExecutor
   
   # The SqlAlchemy connection string to the metadata database.
   # SqlAlchemy supports many different database engine, more information
   # their website
   sql_alchemy_conn = mysql+mysqlconnector://AirFlowClient:sinceJyllandAlgebra812$$@localhost:3306/AirFlowSupport
   ```

4. From shell, run

   ```bash
   airflow initdb
   ```

   Verify that `AirFlowSupport` database now holds multiple tables. 



### Steps: GUI (Sequel Pro)

TODO!



### Steps: Command-line 

TODO!



### 



## Create database for data storage / manipulation

TODO!





## Installing dependencies

```bash
export AIRFLOW_GPL_UNIDECODE=yes
pip install apache-airflow
pip install mysql-connector-python
pip install pony
pip install PyMySQL
pip ist
```



Configure MySQL `explicit_defaults_for_timestamp=1`:

1. First, locate `my.cnf`(MySQL configuration):

   ```bash
   mysql --help|grep -B 3 -A 3 following
   ```

2. Add / ensure the following the line is present in `my.cnf`:

   ```bash
   explicit_defaults_for_timestamp=1
   ```



# Resources

[Getting Started with AirFlow](https://towardsdatascience.com/getting-started-with-apache-airflow-df1aa77d7b1b)

[Stackoverflow: SQLAlchemy + MYSQL + Apache Airflow](https://stackoverflow.com/questions/53225462/apache-airflow-python-3-6-local-executor-mysql-as-a-metadata-database)