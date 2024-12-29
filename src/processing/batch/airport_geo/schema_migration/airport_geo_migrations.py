from pyspark.sql import SparkSession
 
 
def apply_airport_geo_migrations(spark: SparkSession):
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.airport_geo (
        airport_id INT,
        name STRING,
        city STRING,
        country STRING,
        latitude DECIMAL(11, 8),
        longitude DECIMAL(11, 8),
        geolocation STRING
    ) USING iceberg
    """)