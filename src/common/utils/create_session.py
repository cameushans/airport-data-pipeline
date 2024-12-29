from pyspark.sql import SparkSession
def create_spark_session(HDFS: str, WAREHOUSE: str) -> SparkSession :
    spark = SparkSession.builder \
        .appName("KafkaAirportdbBatchProcessing") \
        .config("spark.hadoop.fs.defaultFS", HDFS) \
        .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkCatalog") \
        .config("spark.sql.catalog.spark_catalog.type", "hadoop") \
        .config("spark.sql.catalog.spark_catalog.warehouse", HDFS+WAREHOUSE)\
        .getOrCreate()
        
    spark.sql("CREATE DATABASE IF NOT EXISTS airportdb")

    return spark
