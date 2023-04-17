from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator

default_args = {
    'owner': 'Ying',
    'retries': 2,
    'retry_delay': timedelta(minutes=1)
}
with DAG(dag_id='my-dag-postgres-operator-v1',
         default_args=default_args, start_date=datetime(2022, 8, 1),
         schedule_interval='0 3 * * * *',
         catchup=False) as dag:
    task1 = PostgresOperator(
        task_id='create-postgres-table',
        postgres_conn_id='postgres_localhost',
        sql="""
            create table if not exists dag_runs(
                dt date,
                dag_id character varying,
                primary key (dt, dag_id)
            )        
        """
    )
    task2 = PostgresOperator(
        task_id='insert_into_table',
        postgres_conn_id='postgres_localhost',
        sql="""
        
        """
    )
    task1
