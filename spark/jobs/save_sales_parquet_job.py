from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date


spark = (
    SparkSession.builder
    .appName("Save Sales Parquet Job")
    .getOrCreate()
)

df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "false")
    .csv("/opt/spark/data/sales_data.csv")
)

clean_df = (
    df.withColumn("date", to_date(col("date"), "yyyy-MM-dd"))
      .withColumn("quantity", col("quantity").cast("int"))
      .withColumn("price", col("price").cast("double"))
      .withColumn("product", col("product").cast("string"))
      .withColumn("city", col("city").cast("string"))
      .dropDuplicates()
      .withColumn("total_amount", col("quantity") * col("price"))
)

print("=== Schéma final avant Parquet ===")
clean_df.printSchema()

print("=== Aperçu données finales ===")
clean_df.show()

(
    clean_df.write
    .mode("overwrite")
    .parquet("/opt/spark/data/output/parquet/sales_clean")
)

print("=== Fichier Parquet sauvegardé dans /opt/spark/data/output/parquet/sales_clean ===")

spark.stop()
