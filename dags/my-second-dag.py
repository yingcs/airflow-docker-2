from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'Ying',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}


def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f"Hello World! My name is {first_name} {last_name} and I am {age} years old!")


def get_name(ti):
    ti.xcom_push(key='first_name', value='Jose')
    ti.xcom_push(key='last_name', value='Good Boi')
def get_age(ti):
    ti.xcom_push(key='age', value='6')
with DAG(
        dag_id='my-second-dag-v7',
        default_args=default_args,
        description='Description of my second dag!',
        start_date=datetime(2022, 8, 10),
        schedule_interval='@daily',
        catchup=False) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet
    )
    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )
    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )
    [task2, task3] >> task1
