from pyspark.sql import SparkSession

def apply__booking_migrations(spark: SparkSession):
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.booking (
        booking_id INT,
        flight_id INT,
        seat STRING,
        passenger_id INT,
        price DECIMAL(10, 2)
    ) USING iceberg
    """)