import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://warehouse_user:warehouse_password@localhost:5432/warehouse"
)

df = pd.read_sql("SELECT * FROM sales", engine)

df.to_csv(
    "analytics/exports/sales_export.csv",
    index=False
)

print("CSV export completed")
print(df.shape)
