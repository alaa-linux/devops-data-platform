from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = (
    SparkSession.builder
    .appName("Read Partitioned Parquet Job")
    .getOrCreate()
)

df = spark.read.parquet("/opt/spark/data/output/parquet/sales_partitioned_by_city")

print("=== Schéma Parquet partitionné ===")
df.printSchema()

print("=== Données Parquet ===")
df.show(truncate=False)

print("=== Filtre ville = Marseille ===")
df.filter(col("city") == "Marseille").show(truncate=False)

spark.stop()
