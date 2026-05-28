-- Étape 124.18
-- Index PostgreSQL pour optimiser les agrégations business

CREATE INDEX IF NOT EXISTS idx_sales_sale_date ON sales(sale_date);
CREATE INDEX IF NOT EXISTS idx_sales_product ON sales(product);
CREATE INDEX IF NOT EXISTS idx_sales_city ON sales(city);

CREATE INDEX IF NOT EXISTS idx_incidents_incident_date ON incidents(incident_date);
CREATE INDEX IF NOT EXISTS idx_incidents_description ON incidents(description);

CREATE INDEX IF NOT EXISTS idx_kafka_stats_stat_date ON kafka_stats(stat_date);
CREATE INDEX IF NOT EXISTS idx_kafka_stats_topic_name ON kafka_stats(topic_name);

CREATE INDEX IF NOT EXISTS idx_spark_jobs_job_date ON spark_jobs(job_date);
CREATE INDEX IF NOT EXISTS idx_spark_jobs_status_agg ON spark_jobs(status);

CREATE INDEX IF NOT EXISTS idx_airflow_runs_run_date ON airflow_runs(run_date);
CREATE INDEX IF NOT EXISTS idx_airflow_runs_status_agg ON airflow_runs(status);
