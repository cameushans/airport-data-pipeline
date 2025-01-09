from pyspark.sql import SparkSession

def apply_airport_migrations(spark: SparkSession, key: str):
   spark.sql(f"""
    CREATE TABLE IF NOT EXISTS `{key}` (
        airport_id INT,
        iata STRING,
        icao STRING,
        name STRING
    ) USING iceberg
    """)
