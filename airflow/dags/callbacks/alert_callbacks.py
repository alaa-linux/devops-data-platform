def task_failure_alert(context):
    dag_id = context.get("dag").dag_id
    task_id = context.get("task_instance").task_id
    execution_date = context.get("execution_date")

    print("========================================")
    print("ALERTE AIRFLOW - TASK FAILURE")
    print(f"DAG       : {dag_id}")
    print(f"TASK      : {task_id}")
    print(f"EXECUTION : {execution_date}")
    print("========================================")
