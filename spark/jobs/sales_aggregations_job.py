from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum, count as spark_count, to_date


spark = (
    SparkSession.builder
    .appName("Sales Aggregations Job")
    .getOrCreate()
)

df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "false")
    .csv("/opt/spark/data/sales_data.csv")
)

typed_df = (
    df.withColumn("date", to_date(col("date"), "yyyy-MM-dd"))
      .withColumn("quantity", col("quantity").cast("int"))
      .withColumn("price", col("price").cast("double"))
      .withColumn("product", col("product").cast("string"))
      .withColumn("city", col("city").cast("string"))
)

sales_df = typed_df.withColumn("total_amount", col("quantity") * col("price"))

print("=== CA par produit ===")
(
    sales_df.groupBy("product")
    .agg(
        spark_sum("total_amount").alias("revenue"),
        spark_sum("quantity").alias("total_quantity"),
        spark_count("*").alias("sales_count")
    )
    .orderBy(col("revenue").desc())
    .show()
)

print("=== CA par ville ===")
(
    sales_df.groupBy("city")
    .agg(
        spark_sum("total_amount").alias("revenue"),
        spark_sum("quantity").alias("total_quantity"),
        spark_count("*").alias("sales_count")
    )
    .orderBy(col("revenue").desc())
    .show()
)

print("=== CA total global ===")
(
    sales_df.agg(
        spark_sum("total_amount").alias("global_revenue"),
        spark_sum("quantity").alias("global_quantity"),
        spark_count("*").alias("global_sales_count")
    )
    .show()
)

spark.stop()
