from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Read Batch Outputs Job")
    .getOrCreate()
)

base_path = "/opt/spark/data/output/batch"

outputs = [
    "clean_sales",
    "revenue_by_product",
    "revenue_by_city",
    "global_kpi"
]

for output in outputs:
    print(f"=== Lecture sortie batch : {output} ===")
    df = spark.read.parquet(f"{base_path}/{output}")
    df.printSchema()
    df.show(truncate=False)

spark.stop()
