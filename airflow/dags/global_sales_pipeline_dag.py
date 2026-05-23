from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from callbacks.alert_callbacks import task_failure_alert

default_args = {
    "owner": "alaa",
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
    "on_failure_callback": task_failure_alert,
}

with DAG(
    dag_id="global_sales_pipeline_dag",
    default_args=default_args,
    start_date=datetime(2026, 5, 1),
    schedule="@daily",
    catchup=False,
    tags=["devops-data-platform", "global-pipeline"],
) as dag:

    fetch_api_sales = BashOperator(
        task_id="fetch_api_sales",
        bash_command="python /opt/scripts/ingestion/fetch_api_sales.py "
    )

    run_spark_batch_pipeline = BashOperator(
        task_id="run_spark_batch_pipeline",
        bash_command="bash /opt/scripts/run_batch_pipeline.sh "
    )

    validate_batch_outputs = BashOperator(
        task_id="validate_batch_outputs",
        bash_command="python /opt/scripts/validation/validate_batch_outputs.py "
    )

    load_batch_outputs_to_postgres = BashOperator(
        task_id="load_batch_outputs_to_postgres",
        bash_command="python /opt/scripts/load/load_batch_outputs_to_postgres.py "
    )

    fetch_api_sales >> run_spark_batch_pipeline >> validate_batch_outputs >> load_batch_outputs_to_postgres
