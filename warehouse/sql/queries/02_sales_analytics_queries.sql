-- Chiffre d'affaires par ville
SELECT
    city_name,
    SUM(total_amount) AS revenue
FROM analytics.sales_clean
GROUP BY city_name
ORDER BY revenue DESC;

-- Chiffre d'affaires par produit
SELECT
    product_name,
    SUM(total_amount) AS revenue
FROM analytics.sales_clean
GROUP BY product_name
ORDER BY revenue DESC;

-- Analyse du plan d'exécution
EXPLAIN ANALYZE
SELECT
    product_name,
    SUM(total_amount) AS revenue
FROM analytics.sales_clean
GROUP BY product_name
ORDER BY revenue DESC;
