-- Étape 125.6
-- Rapport SQL Airflow

SELECT
    run_date,
    dag_name,
    status,
    duration_seconds
FROM airflow_runs
ORDER BY run_date, dag_name;
