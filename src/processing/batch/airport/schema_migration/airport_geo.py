from pyspark.sql import SparkSession

def apply_airport_migrations(spark: SparkSession):
   spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.airport (
        airport_id INT,
        iata STRING,
        icao STRING,
        name STRING
    ) USING iceberg
    """)
