from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "alaa",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="validation_sales_dag",
    default_args=default_args,
    start_date=datetime(2026, 5, 1),
    schedule=None,
    catchup=False,
    tags=["devops-data-platform", "validation"],
) as dag:

    validate_batch_outputs = BashOperator(
        task_id="validate_batch_outputs",
        bash_command="python /opt/scripts/validation/validate_batch_outputs.py "
    )

    validate_batch_outputs
