-- =========================================
-- PLATFORM ANALYTICS VIEWS
-- DevOps Data Platform
-- Étape 123 complément strict roadmap
-- =========================================

-- Création tables analytiques techniques de démonstration

CREATE TABLE IF NOT EXISTS incidents (
    incident_id SERIAL PRIMARY KEY,
    incident_date DATE,
    severity TEXT,
    source TEXT,
    description TEXT
);

CREATE TABLE IF NOT EXISTS metrics (
    metric_id SERIAL PRIMARY KEY,
    metric_date DATE,
    component TEXT,
    metric_name TEXT,
    metric_value NUMERIC(12,2)
);

CREATE TABLE IF NOT EXISTS airflow_runs (
    run_id SERIAL PRIMARY KEY,
    dag_name TEXT,
    run_date DATE,
    status TEXT,
    duration_seconds INTEGER
);

CREATE TABLE IF NOT EXISTS kafka_stats (
    stat_id SERIAL PRIMARY KEY,
    topic_name TEXT,
    stat_date DATE,
    messages_count INTEGER,
    consumer_lag INTEGER
);

CREATE TABLE IF NOT EXISTS spark_jobs (
    job_id SERIAL PRIMARY KEY,
    job_name TEXT,
    job_date DATE,
    status TEXT,
    duration_seconds INTEGER
);

-- Données de démonstration

INSERT INTO incidents (incident_date, severity, source, description)
VALUES
('2026-05-01', 'HIGH', 'airflow', 'DAG ingestion failed'),
('2026-05-02', 'MEDIUM', 'kafka', 'Consumer lag detected'),
('2026-05-03', 'LOW', 'spark', 'Slow batch job')
ON CONFLICT DO NOTHING;

INSERT INTO metrics (metric_date, component, metric_name, metric_value)
VALUES
('2026-05-01', 'postgres', 'query_time_ms', 120),
('2026-05-01', 'kafka', 'throughput_msg_sec', 850),
('2026-05-01', 'spark', 'job_duration_sec', 300)
ON CONFLICT DO NOTHING;

INSERT INTO airflow_runs (dag_name, run_date, status, duration_seconds)
VALUES
('global_sales_pipeline', '2026-05-01', 'success', 180),
('spark_sales_dag', '2026-05-02', 'failed', 60),
('validation_sales_dag', '2026-05-03', 'success', 90)
ON CONFLICT DO NOTHING;

INSERT INTO kafka_stats (topic_name, stat_date, messages_count, consumer_lag)
VALUES
('sales-topic', '2026-05-01', 1000, 12),
('sales-topic', '2026-05-02', 1400, 30),
('logs-topic', '2026-05-03', 800, 5)
ON CONFLICT DO NOTHING;

INSERT INTO spark_jobs (job_name, job_date, status, duration_seconds)
VALUES
('batch_sales_pipeline', '2026-05-01', 'success', 240),
('sales_aggregations_job', '2026-05-02', 'success', 180),
('spark_kafka_streaming_sales', '2026-05-03', 'failed', 75)
ON CONFLICT DO NOTHING;

-- Vues demandées par le micro-plan initial

CREATE OR REPLACE VIEW vw_incidents AS
SELECT *
FROM incidents;

CREATE OR REPLACE VIEW vw_performance AS
SELECT *
FROM metrics;

CREATE OR REPLACE VIEW vw_airflow_jobs AS
SELECT *
FROM airflow_runs;

CREATE OR REPLACE VIEW vw_kafka_metrics AS
SELECT *
FROM kafka_stats;

CREATE OR REPLACE VIEW vw_spark_jobs AS
SELECT *
FROM spark_jobs;
