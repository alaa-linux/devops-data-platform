-- Étape 124.16
-- Agrégations Airflow

SELECT
    run_date,
    status,
    COUNT(*) AS runs_count,
    ROUND(AVG(duration_seconds), 2) AS avg_duration_seconds,
    MIN(duration_seconds) AS min_duration_seconds,
    MAX(duration_seconds) AS max_duration_seconds
FROM airflow_runs
GROUP BY run_date, status
ORDER BY run_date, status;
