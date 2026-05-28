-- =========================================
-- ANALYTICAL METRICS SQL
-- DevOps Data Platform
-- Étape 122
-- =========================================

-- Metric 1 : Nombre total de lignes

SELECT
    COUNT(*) AS total_rows
FROM sales;

-- =========================================

-- Metric 2 : Nombre de produits distincts

SELECT
    COUNT(DISTINCT product) AS distinct_products
FROM sales;

-- =========================================

-- Metric 3 : Nombre de villes distinctes

SELECT
    COUNT(DISTINCT city) AS distinct_cities
FROM sales;

-- =========================================

-- Metric 4 : Quantité moyenne vendue

SELECT
    ROUND(AVG(quantity), 2) AS avg_quantity
FROM sales;

-- =========================================

-- Metric 5 : Prix moyen

SELECT
    ROUND(AVG(price), 2) AS avg_price
FROM sales;

-- =========================================

-- Metric 6 : Revenu moyen par vente

SELECT
    ROUND(AVG(revenue), 2) AS avg_revenue_per_sale
FROM sales;

-- =========================================

-- Metric 7 : Revenu minimum et maximum

SELECT
    MIN(revenue) AS min_revenue,
    MAX(revenue) AS max_revenue
FROM sales;

-- =========================================

-- Metric 8 : Panier moyen par ville

SELECT
    city,
    ROUND(AVG(revenue), 2) AS avg_revenue_by_city
FROM sales
GROUP BY city
ORDER BY avg_revenue_by_city DESC;

-- =========================================

-- Metric 9 : Quantité totale par produit

SELECT
    product,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY product
ORDER BY total_quantity DESC;

-- =========================================

-- Metric 10 : Revenu moyen par produit

SELECT
    product,
    ROUND(AVG(revenue), 2) AS avg_revenue_by_product
FROM sales
GROUP BY product
ORDER BY avg_revenue_by_product DESC;
