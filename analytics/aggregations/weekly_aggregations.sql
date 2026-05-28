-- Étape 124.6
-- Agrégations hebdomadaires business

SELECT
    DATE_TRUNC('week', sale_date)::date AS week_start,
    COUNT(*) AS sales_count,
    SUM(quantity) AS total_quantity,
    SUM(revenue) AS total_revenue,
    ROUND(AVG(revenue), 2) AS avg_revenue
FROM sales
GROUP BY DATE_TRUNC('week', sale_date)
ORDER BY week_start;
