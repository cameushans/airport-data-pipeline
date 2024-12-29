from pyspark.sql import SparkSession
   
def apply_airport_reachable_migrations(spark: SparkSession):
   spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.airport_reachable (
        airport_id INT,
        hops INT
    ) USING iceberg
    """)