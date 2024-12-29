from pyspark.sql import SparkSession
 
def apply_airplane_migrations(spark: SparkSession):
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.airplane (
        airplane_id INT,
        capacity INT,
        type_id INT,
        airline_id INT
        )  USING iceberg
    """)