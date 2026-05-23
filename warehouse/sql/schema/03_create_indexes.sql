CREATE INDEX IF NOT EXISTS idx_fact_sales_date
ON analytics.fact_sales(date_id);

CREATE INDEX IF NOT EXISTS idx_fact_sales_product
ON analytics.fact_sales(product_id);

CREATE INDEX IF NOT EXISTS idx_fact_sales_city
ON analytics.fact_sales(city_id);

CREATE INDEX IF NOT EXISTS idx_fact_sales_total_amount
ON analytics.fact_sales(total_amount);
