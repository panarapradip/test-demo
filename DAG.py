from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args={
    'owner':'pradip',
    'retries':5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='our_first_dag_v3',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2024, 12, 29, 2),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world, this is the first task!"
    )
    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo Hey, i am the 2nd task and i will be running after task 1 is completed."
    )
    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo Hey, i am the 3rd task and i will be running after task 1 is completed and at the same time as task 2."
    )

    #task1.set_downstream(task2)
    #task1.set_downstream(task3)

    #task1 >> task2
    #task1 >> task3

    task1 = [task2, task3]
