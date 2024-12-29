from pyspark.sql import SparkSession
 
def apply_flight_migrations(spark: SparkSession):
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.flight (
        flight_id INT,
        flightno STRING,
        `from` INT,
        `to` INT,
        departure TIMESTAMP,
        arrival TIMESTAMP,
        airline_id INT,
        airplane_id INT
    ) USING iceberg
    """)