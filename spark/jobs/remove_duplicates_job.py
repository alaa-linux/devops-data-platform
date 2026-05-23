from pyspark.sql import SparkSession


spark = (
    SparkSession.builder
    .appName("Remove Duplicates Job")
    .getOrCreate()
)

df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("/opt/spark/data/sales_data.csv")
)

print("=== Nombre lignes avant nettoyage ===")
print(df.count())

clean_df = df.dropDuplicates()

print("=== Nombre lignes après suppression doublons ===")
print(clean_df.count())

print("=== Données nettoyées ===")
clean_df.show()

spark.stop()
