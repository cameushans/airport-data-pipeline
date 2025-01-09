from pyspark.sql.types import StructType, StructField, StringType, IntegerType, BooleanType

flight_schedule_schema = StructType([
    StructField("after", StructType([
        StructField("flightno", StringType(), True),
        StructField("from", IntegerType(), True),
        StructField("to", IntegerType(), True),
        StructField("departure", StringType(), True),
        StructField("arrival", StringType(), True),
        StructField("airline_id", IntegerType(), True),
        StructField("monday", BooleanType(), True),
        StructField("tuesday", BooleanType(), True),
        StructField("wednesday", BooleanType(), True),
        StructField("thursday", BooleanType(), True),
        StructField("friday", BooleanType(), True),
        StructField("saturday", BooleanType(), True),
        StructField("sunday", BooleanType(), True),
    ]), True)
])
