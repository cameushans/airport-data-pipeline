from pyspark.sql import SparkSession

def apply_weather_migrations(spark: SparkSession):
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.weatherdata (
    log_date DATE,
    time TIMESTAMP,  -- Remplacer TIME par TIMESTAMP
    station INTEGER,
    temp DECIMAL(5, 2),
    humidity DECIMAL(5, 2),
    airpressure DECIMAL(10, 2),
    wind DECIMAL(5, 2),
    weather STRING,
    winddirection STRING
    ) USING iceberg;
    """)