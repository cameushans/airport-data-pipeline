from pyspark.sql.types import StructType, StructField, StringType, IntegerType

airline_schema = StructType([
    StructField("airline_id", IntegerType(), True),
    StructField("iata", StringType(), True),
    StructField("airlinename", StringType(), True),
    StructField("base_airport", IntegerType(), True)
])
