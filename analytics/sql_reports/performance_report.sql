-- Étape 125.4
-- Rapport SQL performance plateforme

SELECT
    metric_date,
    component,
    metric_name,
    COUNT(*) AS metric_count,
    ROUND(AVG(metric_value), 2) AS avg_metric_value,
    MIN(metric_value) AS min_metric_value,
    MAX(metric_value) AS max_metric_value
FROM metrics
GROUP BY metric_date, component, metric_name
ORDER BY metric_date, component, metric_name;
