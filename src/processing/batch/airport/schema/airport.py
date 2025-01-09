from pyspark.sql.types import StructType, StructField, StringType, IntegerType

airport_info_schema = StructType([
    StructField("after", StructType([
        StructField("airport_id", IntegerType(), True),
        StructField("iata", IntegerType(), True),
        StructField("icao", IntegerType(), True),
        StructField("name", StringType(), True)
     ]), True)       
])