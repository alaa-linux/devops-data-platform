from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "alaa",
}

with DAG(
    dag_id="test_pipeline_dag",
    default_args=default_args,
    start_date=datetime(2026, 5, 1),
    schedule="@daily",
    catchup=False,
    tags=["devops-data-platform"],
) as dag:

    task_1 = BashOperator(
        task_id="show_date",
        bash_command="date"
    )

    task_2 = BashOperator(
        task_id="show_project_structure",
        bash_command="ls -lah /opt/airflow/dags"
    )

    task_1 >> task_2
