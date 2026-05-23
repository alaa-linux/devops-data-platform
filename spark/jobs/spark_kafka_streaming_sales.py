from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType


spark = (
    SparkSession.builder
    .appName("Spark Kafka Streaming Sales")
    .getOrCreate()
)

schema = StructType([
    StructField("date", StringType(), True),
    StructField("product", StringType(), True),
    StructField("quantity", StringType(), True),
    StructField("price", StringType(), True),
    StructField("city", StringType(), True),
])

raw_df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "kafka:29092")
    .option("subscribe", "sales-topic")
    .option("startingOffsets", "earliest")
    .load()
)

json_df = raw_df.selectExpr("CAST(value AS STRING) as json_value")

sales_df = (
    json_df
    .select(from_json(col("json_value"), schema).alias("data"))
    .select("data.*")
)

query = (
    sales_df.writeStream
    .format("console")
    .outputMode("append")
    .option("truncate", "false")
    .start()
)

query.awaitTermination()
