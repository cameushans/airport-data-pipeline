from pyspark.sql.types import StructType, StructField, StringType, IntegerType, LongType

flight_schema = StructType([
    StructField("after", StructType([
        StructField("flight_id", StringType(), True),
        StructField("flightno", StringType(), True),
        StructField("from", StringType(), True),
        StructField("to", StringType(), True),
        StructField("departure", StringType(), True),
        StructField("arrival", StringType(), True),
        StructField("airline", IntegerType(), True),
        StructField("airplane_id", IntegerType(), True),
    ]), True)
])
