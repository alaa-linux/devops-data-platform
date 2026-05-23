CREATE TABLE IF NOT EXISTS analytics.fact_sales (
    sales_id SERIAL PRIMARY KEY,

    date_id INT NOT NULL,
    product_id INT NOT NULL,
    city_id INT NOT NULL,

    quantity INT NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    total_amount NUMERIC(10, 2) NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_sales_date
        FOREIGN KEY (date_id)
        REFERENCES analytics.dim_date(date_id),

    CONSTRAINT fk_sales_product
        FOREIGN KEY (product_id)
        REFERENCES analytics.dim_product(product_id),

    CONSTRAINT fk_sales_city
        FOREIGN KEY (city_id)
        REFERENCES analytics.dim_city(city_id)
);
