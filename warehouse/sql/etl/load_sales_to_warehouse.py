import csv
import logging
import os
import sys
from datetime import datetime
from pathlib import Path

import psycopg2


CSV_FILE = Path("datasets/csv/sales_data.csv")

DB_CONFIG = {
    "host": os.getenv("WAREHOUSE_DB_HOST", "localhost"),
    "port": int(os.getenv("WAREHOUSE_DB_PORT", "5432")),
    "dbname": os.getenv("WAREHOUSE_DB_NAME", "warehouse"),
    "user": os.getenv("WAREHOUSE_DB_USER", "warehouse_user"),
    "password": os.getenv("WAREHOUSE_DB_PASSWORD", ""),
}

LOG_DIR = Path("logs/warehouse")
LOG_FILE = LOG_DIR / "load_sales_to_warehouse.log"


def setup_logging():
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )


def connect_db():
    return psycopg2.connect(**DB_CONFIG)


def get_or_create_date(cursor, sale_date):
    date_obj = datetime.strptime(sale_date, "%Y-%m-%d").date()

    cursor.execute(
        """
        INSERT INTO analytics.dim_date (full_date, year, month, day)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (full_date) DO NOTHING;
        """,
        (date_obj, date_obj.year, date_obj.month, date_obj.day),
    )

    cursor.execute(
        "SELECT date_id FROM analytics.dim_date WHERE full_date = %s;",
        (date_obj,),
    )

    return cursor.fetchone()[0]


def get_or_create_product(cursor, product_name):
    cursor.execute(
        """
        INSERT INTO analytics.dim_product (product_name)
        VALUES (%s)
        ON CONFLICT (product_name) DO NOTHING;
        """,
        (product_name,),
    )

    cursor.execute(
        "SELECT product_id FROM analytics.dim_product WHERE product_name = %s;",
        (product_name,),
    )

    return cursor.fetchone()[0]


def get_or_create_city(cursor, city_name):
    cursor.execute(
        """
        INSERT INTO analytics.dim_city (city_name)
        VALUES (%s)
        ON CONFLICT (city_name) DO NOTHING;
        """,
        (city_name,),
    )

    cursor.execute(
        "SELECT city_id FROM analytics.dim_city WHERE city_name = %s;",
        (city_name,),
    )

    return cursor.fetchone()[0]


def load_sales_data():
    if not CSV_FILE.exists():
        raise FileNotFoundError(f"Fichier CSV introuvable: {CSV_FILE}")

    connection = connect_db()

    try:
        with connection:
            with connection.cursor() as cursor:
                with CSV_FILE.open("r", encoding="utf-8") as file:
                    reader = csv.DictReader(file)

                    inserted_rows = 0

                    for row in reader:
                        date_id = get_or_create_date(cursor, row["date"])
                        product_id = get_or_create_product(cursor, row["product"])
                        city_id = get_or_create_city(cursor, row["city"])

                        quantity = int(row["quantity"])
                        price = float(row["price"])
                        total_amount = quantity * price

                        cursor.execute(
                            """
                            INSERT INTO analytics.fact_sales (
                                date_id,
                                product_id,
                                city_id,
                                quantity,
                                price,
                                total_amount
                            )
                            VALUES (%s, %s, %s, %s, %s, %s);
                            """,
                            (
                                date_id,
                                product_id,
                                city_id,
                                quantity,
                                price,
                                total_amount,
                            ),
                        )

                        inserted_rows += 1

        logging.info("Chargement terminé: %s lignes insérées", inserted_rows)

    finally:
        connection.close()


def main():
    setup_logging()
    logging.info("ETL sales vers PostgreSQL démarré")

    try:
        load_sales_data()
        logging.info("ETL sales vers PostgreSQL terminé avec succès")

    except Exception:
        logging.exception("ETL sales vers PostgreSQL échoué")
        sys.exit(1)


if __name__ == "__main__":
    main()
