from pyspark.sql import SparkSession

def apply_passenger_migrations(spark: SparkSession):
    spark.sql("""
        CREATE TABLE IF NOT EXISTS airportdb.passenger (
            passenger_id INT,
            passportno STRING,
            firstname STRING,
            lastname STRING
        ) USING iceberg
        """)
