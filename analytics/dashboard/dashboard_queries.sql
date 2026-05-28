-- =========================================
-- DASHBOARD DATASETS SQL
-- DevOps Data Platform
-- Étape 124
-- =========================================

-- Dataset 1 : KPI globaux

SELECT *
FROM vw_sales_global_kpi;

-- =========================================

-- Dataset 2 : Revenu par produit

SELECT *
FROM vw_revenue_by_product;

-- =========================================

-- Dataset 3 : Revenu par ville

SELECT *
FROM vw_revenue_by_city;

-- =========================================

-- Dataset 4 : Ventes journalières

SELECT *
FROM vw_sales_daily;

-- =========================================

-- Dataset 5 : Incidents plateforme

SELECT *
FROM vw_incidents;

-- =========================================

-- Dataset 6 : Performance plateforme

SELECT *
FROM vw_performance;

-- =========================================

-- Dataset 7 : Airflow jobs

SELECT *
FROM vw_airflow_jobs;

-- =========================================

-- Dataset 8 : Kafka metrics

SELECT *
FROM vw_kafka_metrics;

-- =========================================

-- Dataset 9 : Spark jobs

SELECT *
FROM vw_spark_jobs;
