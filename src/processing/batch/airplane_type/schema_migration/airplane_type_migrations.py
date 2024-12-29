from pyspark.sql import SparkSession
   
def apply_airplane_type_migrations(spark: SparkSession):
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.airplane_type (
        type_id INT,
        identifier STRING,
        description STRING
    ) USING iceberg
    """)