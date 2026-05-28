import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://warehouse_user:warehouse_password@localhost:5432/warehouse"
)

query = """
SELECT
    product,
    SUM(revenue) AS total_revenue,
    COUNT(*) AS total_sales
FROM sales
GROUP BY product
ORDER BY total_revenue DESC
"""

df = pd.read_sql(query, engine)

df.to_csv(
    "analytics/exports/dashboard_summary.csv",
    index=False
)

print("Dashboard summary export completed")
print(df)
