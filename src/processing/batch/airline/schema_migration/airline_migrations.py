from pyspark.sql import SparkSession
    
def apply_airline_migrations(spark: SparkSession):
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.airline (
        airline_id INT,
        iata STRING,
        airlinename STRING,
        base_airport INT
    ) USING iceberg
   """)