from datetime import datetime, timedelta
from random import randint
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

default_args = {
'owner':'Ying',
'retries':5,
'retry_delay':timedelta(minutes=1)
}

def _some_model():
    return randint(1,10)
with DAG(
    dag_id='my-first-dag-v7',
    default_args=default_args,
    description='Description of my first dag!',
    start_date=datetime(2022,8,10),
    schedule_interval='@daily',
    catchup=False) as dag:
        task1 = BashOperator(
            task_id = 'first-taskv1',
            bash_command="echo hello world I am the first task")
        task2 = BashOperator(
            task_id = 'second-taskv1',
            bash_command="echo hello world I will be running after the first task")
        task3 = PythonOperator(
            task_id= 'third-taskv1',
            python_callable=_some_model
        )

        #task1.set_downstream(task2)
        #task1.set_downstream(task3)

        task1 >> [task2,task3]
