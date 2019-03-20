# DataPipelines

This repository holds source-code for a sample application, specifically extracting, converting and outputting a dataset. 

Technologies employed

- MySQL
- Python
- Apache AirFlow



## Realize the following - and avoid frustration!

- The database used by AirFlow (in-memory or persisted) backs AirFlow itself, *but has nothing to do with the storage of the (if any) data-tasks carried out by workflows managed by AirFlow*.
  - Hence, if one plans to setup workflows that persists data to a database, two separate / unrelated databases should come into play:
    - one for the AirFlow application / server (always needed) - the "airflow database"
      This database only holds data used to support AirFlow - data going in and out of workflows are *not* to be persisted in this database.
    - (optional, depending on need of workflow) another database for data-storage / manipulation, to be used by workflow tasks - the "data database". 
- AirFlow provides a `MySQLOperator`; that operator allows you to run sql-queries against the "data-database". I suggest one forgets about the eixstence of and/or does *not* use `MySQLOperator` to interact with the database, but rather use an ORM, for instance [PonyORM](https://docs.ponyorm.org). 



## Dataset

Download beer-reviews dataset in local folder `data`

```bash
mkdir data/
cd data
curl https://s3.eu-west-2.amazonaws.com/tgtg-public-data/beer_reviews.csv.zip -o beer_reviews.csv.zip
unzip beer_reviews.csv.zip
```



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

   Verify that `AirFlowSupport` now holds multiple tables. 



### Steps: GUI (Sequel Pro)

TODO!



### Steps: Command-line 

TODO!



### 



## Create database for data storage / manipulation

```bash

```





## Installing dependencies

```bash
export AIRFLOW_GPL_UNIDECODE=yes
pip install apache-airflow
pip install mysql-connector-python
pip install pony
pip install PyMySQL
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