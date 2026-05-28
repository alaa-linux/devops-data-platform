import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://warehouse_user:warehouse_password@localhost:5432/warehouse"
)

query = """
SELECT
    product,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC
"""

df = pd.read_sql(query, engine)

plt.figure(figsize=(8,5))

plt.bar(
    df["product"],
    df["total_revenue"]
)

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

output_path = "analytics/pdf_reports/revenue_chart.png"

plt.savefig(output_path)

print(f"Chart generated: {output_path}")
