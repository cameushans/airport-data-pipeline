from pyspark.sql.types import StructType, StructField, StringType, IntegerType, LongType

passenger_details_schema = StructType([
    StructField("after", StructType([
        StructField("passenger_id", IntegerType(), True),
        StructField("birthdate", IntegerType(), True),
        StructField("sex", StringType(), True),
        StructField("street", StringType(), True),
        StructField("city", StringType(), True),
        StructField("zip", IntegerType(), True),
        StructField("country", StringType(), True),
        StructField("emailadress", StringType(), True),
        StructField("telephoneno", StringType(), True)
    ]), True),
])