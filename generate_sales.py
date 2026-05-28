import random
import time
from datetime import datetime

import psycopg2

products = {
    "Laptop": 1200,
    "Mouse": 25,
    "Keyboard": 75,
    "Monitor": 300,
}

cities = [
    "Marseille",
    "Paris",
    "Lyon",
    "Nice",
    "Bordeaux",
    "Lille",
    "Nantes",
    "Toulouse",
]

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="warehouse",
    user="warehouse_user",
    password="warehouse_password",
)

cursor = conn.cursor()

print("[INFO] Real-time sales generator started...")

while True:
    product = random.choice(list(products.keys()))
    price = products[product]
    quantity = random.randint(1, 10)
    city = random.choice(cities)
    revenue = quantity * price

    cursor.execute(
        """
        INSERT INTO sales (
            sale_date,
            product,
            quantity,
            price,
            city,
            revenue
        )
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (
            datetime.now().date(),
            product,
            quantity,
            price,
            city,
            revenue,
        ),
    )

    conn.commit()

    print(f"[INSERTED] {datetime.now()} | {product} | {city} | qty={quantity} | revenue={revenue}")

    time.sleep(5)

