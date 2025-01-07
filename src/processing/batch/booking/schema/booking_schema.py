from pyspark.sql.types import StructType, StructField, StringType, IntegerType, LongType, DoubleType


booking_schema = StructType([
    StructField("before", StructType([
        StructField("booking_id", IntegerType(), True),
        StructField("flight_id", StringType(), True),
        StructField("seat", StringType(), True),
        StructField("passenger_id", IntegerType(), True),
        StructField("price", DoubleType(), True)
    ]), True)
])