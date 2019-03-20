from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from dataloader import read_csv_file


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

containing_workflow = DAG('Import CSV',
                          default_args=default_args,
                          schedule_interval=datetime.timedelta(days=1))

firstTask = PythonOperator(
    task_id='Load_CSV_rows',
    python_callable=read_csv_file,
    dag=containing_workflow
)
