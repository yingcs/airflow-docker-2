from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Ying',
    'retries': 2,
    'retry_delay': timedelta(minutes=1)
}

with DAG(dag_id='my-dag-catchup-and-backfill-v3-3',
         default_args=default_args, start_date=datetime(2022, 8, 1),
         schedule_interval='0 3 * * Tue,Fri',
         catchup=False) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo This is a bash task'
    )
