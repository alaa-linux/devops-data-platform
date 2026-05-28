-- KPI Anomaly Alert Rules

SELECT *
FROM vw_kpi_alerts
WHERE alert_status IN ('WARNING', 'CRITICAL');
