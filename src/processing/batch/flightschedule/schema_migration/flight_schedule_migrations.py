from pyspark.sql import SparkSession
 
def apply_flight_schedule_migrations(spark: SparkSession):
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.flightschedule (
        flightno STRING,
        from INT,
        to INT,
        departure STRING,
        arrival STRING,
        airline_id INT,
        monday BOOLEAN,
        tuesday BOOLEAN,
        wednesday BOOLEAN,
        thursday BOOLEAN,
        friday BOOLEAN,
        saturday BOOLEAN,
        sunday BOOLEAN
    ) USING iceberg
    """)