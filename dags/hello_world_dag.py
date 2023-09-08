from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def hello_world():
    print(hello_world)


with DAG(
    dag_id='hello_world_dag',
    start_date=datetime(2022, 1, 1),
    schedule_interval='@hourly',
    catchup=False,
) as dag:

    hello_world_task = PythonOperator(
        task_id='hello_world_task', python_callable=hello_world
    )
