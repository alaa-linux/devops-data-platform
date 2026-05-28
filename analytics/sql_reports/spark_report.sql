-- Étape 125.10
-- Rapport SQL Spark

SELECT
    job_date,
    job_name,
    status,
    duration_seconds
FROM spark_jobs
ORDER BY job_date, job_name;
