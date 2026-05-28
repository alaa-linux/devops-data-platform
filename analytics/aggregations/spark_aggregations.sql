-- Étape 124.14
-- Agrégations Spark

SELECT
    job_date,
    status,
    COUNT(*) AS jobs_count,
    ROUND(AVG(duration_seconds), 2) AS avg_duration_seconds,
    MIN(duration_seconds) AS min_duration_seconds,
    MAX(duration_seconds) AS max_duration_seconds
FROM spark_jobs
GROUP BY job_date, status
ORDER BY job_date, status;
