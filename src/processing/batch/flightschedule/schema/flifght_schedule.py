from pyspark.sql.types import StructType, StructField, StringType, IntegerType, BooleanType

flight_schedule_schema = StructType([
    StructField("after", StructType([
        StructField("flightno", StringType(), True),
        StructField("from", IntegerType(), True),
        StructField("to", IntegerType(), True),
        StructField("departure", StringType(), True),
        StructField("arrival", StringType(), True),
        StructField("airline_id", IntegerType(), True),
        StructField("monday", StringType(), True),
        StructField("tuesday", StringType(), True),
        StructField("wednesday", StringType(), True),
        StructField("thursday", StringType(), True),
        StructField("friday", StringType(), True),
        StructField("saturday", StringType(), True),
        StructField("sunday", StringType(), True),
    ]), True)
])
