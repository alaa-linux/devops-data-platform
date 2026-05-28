-- Étape 124.2
-- Agrégations journalières

SELECT
    sale_date,
    COUNT(*) AS sales_count,
    SUM(quantity) AS total_quantity,
    SUM(revenue) AS total_revenue,
    ROUND(AVG(revenue), 2) AS avg_revenue
FROM sales
GROUP BY sale_date
ORDER BY sale_date;
