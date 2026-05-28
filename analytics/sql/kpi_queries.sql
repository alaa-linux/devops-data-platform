-- =========================================
-- KPI SQL QUERIES
-- DevOps Data Platform
-- =========================================

-- KPI 1 : Chiffre d'affaires total

SELECT
    SUM(revenue) AS total_revenue
FROM sales;

-- =========================================

-- KPI 2 : Quantité totale vendue

SELECT
    SUM(quantity) AS total_quantity
FROM sales;

-- =========================================

-- KPI 3 : Nombre total de ventes

SELECT
    COUNT(*) AS total_sales
FROM sales;

-- =========================================

-- KPI 4 : Top produits par revenu

SELECT
    product,
    SUM(revenue) AS revenue_by_product
FROM sales
GROUP BY product
ORDER BY revenue_by_product DESC;

-- =========================================

-- KPI 5 : Chiffre d'affaires par ville

SELECT
    city,
    SUM(revenue) AS revenue_by_city
FROM sales
GROUP BY city
ORDER BY revenue_by_city DESC;

-- =========================================

-- KPI 6 : Quantité moyenne vendue

SELECT
    AVG(quantity) AS average_quantity
FROM sales;

-- =========================================

-- KPI 7 : Prix moyen

SELECT
    AVG(price) AS average_price
FROM sales;

-- =========================================

-- KPI 8 : Nombre de ventes par catégorie

SELECT
    category,
    COUNT(*) AS sales_count
FROM sales
GROUP BY category
ORDER BY sales_count DESC;

-- =========================================

-- KPI 9 : Meilleure ville en revenu

SELECT
    city,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY city
ORDER BY total_revenue DESC
LIMIT 1;

-- =========================================

-- KPI 10 : Produit le plus vendu

SELECT
    product,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY product
ORDER BY total_quantity DESC
LIMIT 1;
