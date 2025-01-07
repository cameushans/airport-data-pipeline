from pyspark.sql.types import StructType, StructField, StringType, IntegerType, LongType, TimestampType

flight_log_schema = StructType([
    StructField("before", StructType([
        StructField("flight_log_id", LongType(), True),
        StructField("log_date", TimestampType(), True),
        StructField("user", StringType(), True),
        StructField("flight_id", IntegerType(), True),
        StructField("flightno_old", StringType(), True),
        StructField("flightno_new", StringType(), True),
        StructField("from_old", IntegerType(), True),
        StructField("to_old", IntegerType(), True),
        StructField("from_new", IntegerType(), True),
        StructField("to_new", IntegerType(), True),
        StructField("departure_old", TimestampType(), True),
        StructField("arrival_old", TimestampType(), True),
        StructField("departure_new", TimestampType(), True),
        StructField("arrival_new", TimestampType(), True),
        StructField("airplane_id_old", IntegerType(), True),
        StructField("airplane_id_new", IntegerType(), True),
        StructField("airline_id_old", IntegerType(), True),
        StructField("airline_id_new", IntegerType(), True),
        StructField("comment", StringType(), True),
    ]), True)
])
