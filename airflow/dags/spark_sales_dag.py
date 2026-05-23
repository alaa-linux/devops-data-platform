from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "alaa",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="spark_sales_dag",
    default_args=default_args,
    start_date=datetime(2026, 5, 1),
    schedule=None,
    catchup=False,
    tags=["devops-data-platform", "spark"],
) as dag:

    run_spark_batch_pipeline = BashOperator(
        task_id="run_spark_batch_pipeline",
        bash_command="bash /opt/scripts/run_batch_pipeline.sh "
    )

    run_spark_batch_pipeline
