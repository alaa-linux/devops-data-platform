from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, sum as spark_sum, count as spark_count


spark = (
    SparkSession.builder
    .appName("Batch Sales Pipeline Job")
    .config("spark.sql.shuffle.partitions", "4")
    .getOrCreate()
)

input_path = "/opt/spark/data/sales_data.csv"
output_base_path = "/opt/spark/data/output/batch"

raw_df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "false")
    .csv(input_path)
)

clean_df = (
    raw_df.withColumn("date", to_date(col("date"), "yyyy-MM-dd"))
          .withColumn("quantity", col("quantity").cast("int"))
          .withColumn("price", col("price").cast("double"))
          .withColumn("product", col("product").cast("string"))
          .withColumn("city", col("city").cast("string"))
          .dropDuplicates()
          .withColumn("total_amount", col("quantity") * col("price"))
)

revenue_by_product_df = (
    clean_df.groupBy("product")
    .agg(
        spark_sum("total_amount").alias("revenue"),
        spark_sum("quantity").alias("total_quantity"),
        spark_count("*").alias("sales_count")
    )
    .orderBy(col("revenue").desc())
)

revenue_by_city_df = (
    clean_df.groupBy("city")
    .agg(
        spark_sum("total_amount").alias("revenue"),
        spark_sum("quantity").alias("total_quantity"),
        spark_count("*").alias("sales_count")
    )
    .orderBy(col("revenue").desc())
)

global_kpi_df = (
    clean_df.agg(
        spark_sum("total_amount").alias("global_revenue"),
        spark_sum("quantity").alias("global_quantity"),
        spark_count("*").alias("global_sales_count")
    )
)

print("=== Données nettoyées ===")
clean_df.show(truncate=False)

print("=== CA par produit ===")
revenue_by_product_df.show(truncate=False)

print("=== CA par ville ===")
revenue_by_city_df.show(truncate=False)

print("=== KPI global ===")
global_kpi_df.show(truncate=False)

clean_df.write.mode("overwrite").parquet(f"{output_base_path}/clean_sales")
revenue_by_product_df.write.mode("overwrite").parquet(f"{output_base_path}/revenue_by_product")
revenue_by_city_df.write.mode("overwrite").parquet(f"{output_base_path}/revenue_by_city")
global_kpi_df.write.mode("overwrite").parquet(f"{output_base_path}/global_kpi")

print(f"=== Pipeline batch terminé. Résultats sauvegardés dans {output_base_path} ===")

spark.stop()
