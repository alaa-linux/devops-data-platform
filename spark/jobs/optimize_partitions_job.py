from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date


spark = (
    SparkSession.builder
    .appName("Optimize Partitions Job")
    .config("spark.sql.shuffle.partitions", "4")
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

print("=== Nombre de partitions au chargement ===")
print(clean_df.rdd.getNumPartitions())

optimized_df = clean_df.repartition(2, col("city"))

print("=== Nombre de partitions après optimisation ===")
print(optimized_df.rdd.getNumPartitions())

(
    optimized_df.write
    .mode("overwrite")
    .partitionBy("city")
    .parquet("/opt/spark/data/output/parquet/sales_partitioned_by_city")
)

print("=== Données sauvegardées en Parquet partitionné par ville ===")

spark.stop()
