from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum


spark = (
    SparkSession.builder
    .appName("First Sales Spark Job")
    .getOrCreate()
)

df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("/opt/spark/data/sales_data.csv")
)

df = df.withColumn("total_amount", col("quantity") * col("price"))

print("=== Données chargées ===")
df.show()

print("=== Chiffre d'affaires par produit ===")
(
    df.groupBy("product")
    .agg(spark_sum("total_amount").alias("revenue"))
    .orderBy(col("revenue").desc())
    .show()
)

spark.stop()
