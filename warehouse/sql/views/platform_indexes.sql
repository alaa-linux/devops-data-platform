-- =========================================
-- PLATFORM ANALYTICS INDEXES
-- DevOps Data Platform
-- Étape 123.8
-- =========================================

CREATE INDEX IF NOT EXISTS idx_incidents_date ON incidents(incident_date);
CREATE INDEX IF NOT EXISTS idx_incidents_source ON incidents(source);

CREATE INDEX IF NOT EXISTS idx_metrics_component ON metrics(component);
CREATE INDEX IF NOT EXISTS idx_metrics_date ON metrics(metric_date);

CREATE INDEX IF NOT EXISTS idx_airflow_runs_status ON airflow_runs(status);
CREATE INDEX IF NOT EXISTS idx_airflow_runs_date ON airflow_runs(run_date);

CREATE INDEX IF NOT EXISTS idx_kafka_stats_topic ON kafka_stats(topic_name);
CREATE INDEX IF NOT EXISTS idx_kafka_stats_date ON kafka_stats(stat_date);

CREATE INDEX IF NOT EXISTS idx_spark_jobs_status ON spark_jobs(status);
CREATE INDEX IF NOT EXISTS idx_spark_jobs_date ON spark_jobs(job_date);
