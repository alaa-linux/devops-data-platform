CREATE OR REPLACE VIEW vw_duplicate_rows AS
SELECT
    COUNT(*) AS duplicate_rows
FROM (
    SELECT
        sale_date,
        product,
        city,
        revenue,
        COUNT(*) AS row_count
    FROM sales
    GROUP BY sale_date, product, city, revenue
    HAVING COUNT(*) > 1
) d;

CREATE OR REPLACE VIEW vw_sales_anomalies AS
SELECT
    COUNT(*) AS anomaly_count
FROM sales
WHERE revenue > 10000;


CREATE OR REPLACE VIEW vw_ingestion_quality AS
SELECT
    COUNT(*) AS total_ingested_rows
FROM sales;


CREATE OR REPLACE VIEW vw_quality_alerts AS
SELECT
    CASE
        WHEN COUNT(*) > 20 THEN 'ALERT'
        ELSE 'OK'
    END AS quality_status
FROM sales
WHERE revenue > 10000;


CREATE OR REPLACE VIEW vw_kpi_alerts AS
SELECT
    'anomalies' AS kpi_name,
    anomaly_count AS kpi_value,
    CASE
        WHEN anomaly_count > 20 THEN 'CRITICAL'
        WHEN anomaly_count > 10 THEN 'WARNING'
        ELSE 'OK'
    END AS alert_status
FROM vw_sales_anomalies

UNION ALL

SELECT
    'duplicate_rows' AS kpi_name,
    duplicate_rows AS kpi_value,
    CASE
        WHEN duplicate_rows > 100 THEN 'CRITICAL'
        WHEN duplicate_rows > 50 THEN 'WARNING'
        ELSE 'OK'
    END AS alert_status
FROM vw_duplicate_rows

UNION ALL

SELECT
    'total_nulls' AS kpi_name,
    total_nulls AS kpi_value,
    CASE
        WHEN total_nulls > 5 THEN 'CRITICAL'
        WHEN total_nulls > 0 THEN 'WARNING'
        ELSE 'OK'
    END AS alert_status
FROM (
    SELECT
        (
            COUNT(*) FILTER (WHERE product IS NULL)
            +
            COUNT(*) FILTER (WHERE city IS NULL)
            +
            COUNT(*) FILTER (WHERE revenue IS NULL)
        ) AS total_nulls
    FROM sales
) n

UNION ALL

SELECT
    'ingestion_rows' AS kpi_name,
    total_ingested_rows AS kpi_value,
    CASE
        WHEN total_ingested_rows < 100 THEN 'CRITICAL'
        ELSE 'OK'
    END AS alert_status
FROM vw_ingestion_quality;
