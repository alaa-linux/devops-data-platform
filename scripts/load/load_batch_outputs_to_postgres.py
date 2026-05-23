import os
from pathlib import Path

import pandas as pd
import psycopg2
from psycopg2 import sql

BASE_PATH = Path("/opt/spark/data/output/batch")

DB_CONFIG = {
    "host": os.getenv("WAREHOUSE_DB_HOST", "postgres-warehouse"),
    "port": int(os.getenv("WAREHOUSE_DB_PORT", "5432")),
    "dbname": os.getenv("WAREHOUSE_DB_NAME", "warehouse"),
    "user": os.getenv("WAREHOUSE_DB_USER", "warehouse_user"),
    "password": os.getenv("WAREHOUSE_DB_PASSWORD", ""),
}

TABLES = {
    "revenue_by_product": "analytics_revenue_by_product",
    "revenue_by_city": "analytics_revenue_by_city",
    "global_kpi": "analytics_global_kpi",
}

CREATE_TABLES_SQL = {
    "analytics_revenue_by_product": """
        CREATE TABLE IF NOT EXISTS analytics_revenue_by_product (
            product TEXT,
            revenue DOUBLE PRECISION,
            total_quantity BIGINT,
            sales_count BIGINT
        );
    """,
    "analytics_revenue_by_city": """
        CREATE TABLE IF NOT EXISTS analytics_revenue_by_city (
            city TEXT,
            revenue DOUBLE PRECISION,
            total_quantity BIGINT,
            sales_count BIGINT
        );
    """,
    "analytics_global_kpi": """
        CREATE TABLE IF NOT EXISTS analytics_global_kpi (
            global_revenue DOUBLE PRECISION,
            global_quantity BIGINT,
            global_sales_count BIGINT
        );
    """,
}


def read_parquet_dataset(dataset_name):
    dataset_path = BASE_PATH / dataset_name
    parquet_files = list(dataset_path.glob("*.parquet"))

    if not parquet_files:
        raise FileNotFoundError(f"Aucun fichier parquet trouvé pour {dataset_name}")

    return pd.concat([pd.read_parquet(file) for file in parquet_files], ignore_index=True)


with psycopg2.connect(**DB_CONFIG) as conn:
    with conn.cursor() as cur:
        for table_name, create_sql in CREATE_TABLES_SQL.items():
            cur.execute(create_sql)
            # nosemgrep: python.sqlalchemy.security.sqlalchemy-execute-raw-query.sqlalchemy-execute-raw-query
            cur.execute(
                sql.SQL("TRUNCATE TABLE {};").format(
                    sql.Identifier(table_name)
                )
            )

        for dataset_name, table_name in TABLES.items():
            df = read_parquet_dataset(dataset_name)

            columns = list(df.columns)
            placeholders = sql.SQL(", ").join(sql.Placeholder() * len(columns))
            columns_sql = sql.SQL(", ").join(
                sql.Identifier(column) for column in columns
            )

            insert_sql = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
                sql.Identifier(table_name),
                columns_sql,
                placeholders,
            )

            rows = [tuple(row) for row in df.to_numpy()]
            cur.executemany(insert_sql, rows)

            print(f"{table_name} chargé : {len(rows)} lignes")

print("Chargement SQL terminé avec succès")
