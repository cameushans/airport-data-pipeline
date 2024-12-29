from pyspark.sql.types import StructType, StructField, StringType, IntegerType, LongType


passenger_schema = StructType([
    StructField("before", StructType([
        StructField("passenger_id", IntegerType(), True),
        StructField("passportno", StringType(), True),
        StructField("firstname", StringType(), True),
        StructField("lastname", StringType(), True)
    ]), True),
    StructField("after", StructType([
        StructField("passenger_id", IntegerType(), True),
        StructField("passportno", StringType(), True),
        StructField("firstname", StringType(), True),
        StructField("lastname", StringType(), True)
    ]), True)
])