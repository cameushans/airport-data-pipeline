from pyspark.sql.types import StructType, StructField, StringType, IntegerType

airport_info_schema = StructType([
    StructField("airport_id", IntegerType(), True),
    StructField("iata", StringType(), True),
    StructField("icao", StringType(), True),
    StructField("name", StringType(), True)
])