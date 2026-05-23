from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "alaa",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="ingestion_sales_dag",
    default_args=default_args,
    start_date=datetime(2026, 5, 1),
    schedule=None,
    catchup=False,
    tags=["devops-data-platform", "ingestion"],
) as dag:

    fetch_api_sales = BashOperator(
        task_id="fetch_api_sales",
        bash_command="python /opt/scripts/ingestion/fetch_api_sales.py"
    )

    fetch_api_sales
