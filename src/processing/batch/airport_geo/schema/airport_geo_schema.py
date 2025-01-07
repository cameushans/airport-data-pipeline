from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DecimalType

airport_details_schema = StructType([
    StructField("before", StructType([
        StructField("airport_id", IntegerType(), True),
        StructField("name", StringType(), True),
        StructField("city", StringType(), True),
        StructField("country", StringType(), True),
        StructField("latitude", DecimalType(11, 8), True),
        StructField("longitude", DecimalType(11, 8), True),
        StructField("geolocation", StringType(), True)
    ]), True)
])
