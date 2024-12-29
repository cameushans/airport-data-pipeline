from pyspark.sql import SparkSession
import pyspark.sql.functions as psf 
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, LongType

# Créer une session Spark
spark = SparkSession.builder \
    .appName("KafkaBatchProcessing") \
    .getOrCreate()

kafka_bootstrap_servers = "192.168.121.142:9092,192.168.121.51:9092,192.168.121.141:9092"
topic_name = "mysql-airportdb.airportdb.passenger"  

# Lire les messages Kafka
kafka_df = spark.read \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribePattern", topic_name) \
    .option("startingOffsets", "earliest") \
    .load() \
    
print(kafka_df.schema)
''' # Convertir la colonne 'value' de type binaire en chaîne de caractères
kafka_df = kafka_df.selectExpr("CAST(value AS STRING) as value")

print("Début du traitement...", kafka_df)
payload_schema = StructType([
    StructField("before", StructType([
        StructField("passenger_id", IntegerType(), True),
        StructField("passportno", StringType(), True),
        StructField("firstname", StringType(), True),
        StructField("lastname", StringType(), True)
    ]), True),
    StructField("after", StructType([
        StructField("passenger_id", IntegerType(), True),
        StructField("passportno", StringType(), True),
        StructField("firstname", StringType(), True),
        StructField("lastname", StringType(), True)
    ]), True),
    StructField("source", StructType([
        StructField("version", StringType(), True),
        StructField("connector", StringType(), True),
        StructField("name", StringType(), True),
        StructField("ts_ms", LongType(), True),
        StructField("snapshot", StringType(), True),
        StructField("db", StringType(), True),
        StructField("sequence", StringType(), True),
        StructField("table", StringType(), True),
        StructField("server_id", LongType(), True),
        StructField("gtid", StringType(), True),
        StructField("file", StringType(), True),
        StructField("pos", LongType(), True),
        StructField("row", IntegerType(), True),
        StructField("thread", LongType(), True),
        StructField("query", StringType(), True)
    ]), True),
    StructField("op", StringType(), True),
    StructField("ts_ms", LongType(), True),
    StructField("transaction", StructType([
        StructField("id", StringType(), True),
        StructField("total_order", LongType(), True),
        StructField("data_collection_order", LongType(), True)
    ]), True)
])


kafka_df \
  .select(psf.get_json_object(kafka_df['value'],"$.payload").alias('payload')) \
  .select(psf.from_json(psf.col('payload'), payload_schema).alias("DF")) \
  .select("DF.*") \
  .show(10)  
# Définir un schéma JSON valide

# Appliquer le schéma pour analyser les données JSON

 '''