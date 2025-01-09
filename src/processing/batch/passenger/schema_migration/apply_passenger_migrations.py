from pyspark.sql import SparkSession

def apply_passenger_migrations(spark: SparkSession, domain: str):
    spark.sql(f"""
        CREATE TABLE IF NOT EXISTS {domain} (
            passenger_id INT,
            passportno STRING,
            firstname STRING,
            lastname STRING
        ) USING iceberg
        """)
