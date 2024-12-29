from pyspark.sql import SparkSession
def apply_flight_log_migrations(spark: SparkSession):
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.flight_log (
    flight_log_id BIGINT,
    log_date TIMESTAMP,
    user STRING,
    flight_id INT,
    flightno_old STRING,
    flightno_new STRING,
    from_old INT,
    to_old INT,
    from_new INT,
    to_new INT,
    departure_old TIMESTAMP,
    arrival_old TIMESTAMP,
    departure_new TIMESTAMP,
    arrival_new TIMESTAMP,
    airplane_id_old INT,
    airplane_id_new INT,
    airline_id_old INT,
    airline_id_new INT,
    comment STRING
  ) USING iceberg
  """)