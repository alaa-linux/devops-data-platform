CREATE OR REPLACE VIEW analytics.sales_clean AS
SELECT
    f.sales_id,
    d.full_date,
    d.year,
    d.month,
    d.day,
    p.product_name,
    c.city_name,
    f.quantity,
    f.price,
    f.total_amount,
    f.created_at
FROM analytics.fact_sales f
JOIN analytics.dim_date d
    ON f.date_id = d.date_id
JOIN analytics.dim_product p
    ON f.product_id = p.product_id
JOIN analytics.dim_city c
    ON f.city_id = c.city_id;
