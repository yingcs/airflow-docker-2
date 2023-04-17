from datetime import datetime, timedelta
from airflow.decorators import dag, task

default_args = {
    'owner': 'Ying',
    'retries': 2,
    'retry_delay': timedelta(minutes=1)
}
@dag(dag_id='my-taskflow-dag-v2',
        default_args=default_args,
        start_date=datetime(2022, 8, 10),
        schedule_interval='@daily')

def something():
    
    @task(multiple_outputs=True)
    def get_name():
        return {'first_name':'Poncho', 'last_name':'Good Boi'}

    @task()
    def get_age():
        return 1

    @task()
    def greet(first_name, last_name, age):
        print(f"Hello world! My name is {first_name} {last_name} "
            f"and I am {age} years old")

    name = get_name()
    age = get_age()
    greet(first_name=name['first_name'],last_name=name['last_name'], age=age)

greet_dag = something()