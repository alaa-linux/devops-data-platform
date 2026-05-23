from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date


spark = (
    SparkSession.builder
    .appName("Fix Column Types Job")
    .getOrCreate()
)

df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "false")
    .csv("/opt/spark/data/sales_data.csv")
)

print("=== Schéma avant correction ===")
df.printSchema()

typed_df = (
    df.withColumn("date", to_date(col("date"), "yyyy-MM-dd"))
      .withColumn("quantity", col("quantity").cast("int"))
      .withColumn("price", col("price").cast("double"))
      .withColumn("product", col("product").cast("string"))
      .withColumn("city", col("city").cast("string"))
)

print("=== Schéma après correction ===")
typed_df.printSchema()

print("=== Données typées ===")
typed_df.show()

spark.stop()
