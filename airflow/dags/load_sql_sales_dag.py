from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "alaa",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="load_sql_sales_dag",
    default_args=default_args,
    start_date=datetime(2026, 5, 1),
    schedule=None,
    catchup=False,
    tags=["devops-data-platform", "sql", "warehouse"],
) as dag:

    load_batch_outputs_to_postgres = BashOperator(
        task_id="load_batch_outputs_to_postgres",
        bash_command="python /opt/scripts/load/load_batch_outputs_to_postgres.py "
    )

    load_batch_outputs_to_postgres
