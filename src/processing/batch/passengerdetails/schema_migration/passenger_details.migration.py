
from pyspark.sql import SparkSession


def apply_migrations(spark: SparkSession):
    spark.sql("""
         CREATE TABLE IF NOT EXISTS airportdb.passengerdetails (
            passenger_id INT,
            birthdate STRING,
            sex STRING,
            street STRING,
            city STRING,
            zip INT,
            country STRING,
            emailadress STRING,
            telephoneno STRING
        ) USING iceberg
        """)
    
    