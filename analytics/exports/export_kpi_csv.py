import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://warehouse_user:warehouse_password@localhost:5432/warehouse"
)

query = """
SELECT *
FROM vw_kpi_alerts
"""

df = pd.read_sql(query, engine)

df.to_csv(
    "analytics/exports/kpi_alerts_export.csv",
    index=False
)

print("KPI CSV export completed")
print(df)
