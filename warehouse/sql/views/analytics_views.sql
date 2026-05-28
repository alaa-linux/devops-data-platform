-- =========================================
-- ANALYTICS SQL VIEWS
-- DevOps Data Platform
-- Étape 123
-- =========================================

-- Vue 1 : KPI globaux ventes

CREATE OR REPLACE VIEW vw_sales_global_kpi AS
SELECT
    COUNT(*) AS total_sales,
    SUM(quantity) AS total_quantity,
    SUM(revenue) AS total_revenue,
    ROUND(AVG(revenue), 2) AS avg_revenue_per_sale,
    MIN(revenue) AS min_revenue,
    MAX(revenue) AS max_revenue
FROM sales;

-- =========================================

-- Vue 2 : Revenu par produit

CREATE OR REPLACE VIEW vw_revenue_by_product AS
SELECT
    product,
    SUM(quantity) AS total_quantity,
    SUM(revenue) AS total_revenue,
    ROUND(AVG(revenue), 2) AS avg_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC;

-- =========================================

-- Vue 3 : Revenu par ville

CREATE OR REPLACE VIEW vw_revenue_by_city AS
SELECT
    city,
    COUNT(*) AS sales_count,
    SUM(quantity) AS total_quantity,
    SUM(revenue) AS total_revenue,
    ROUND(AVG(revenue), 2) AS avg_revenue
FROM sales
GROUP BY city
ORDER BY total_revenue DESC;

-- =========================================

-- Vue 4 : Ventes par jour

CREATE OR REPLACE VIEW vw_sales_daily AS
SELECT
    sale_date,
    COUNT(*) AS sales_count,
    SUM(quantity) AS total_quantity,
    SUM(revenue) AS total_revenue,
    ROUND(AVG(revenue), 2) AS avg_revenue
FROM sales
GROUP BY sale_date
ORDER BY sale_date;
