from pyspark.sql.types import StructType, StructField, IntegerType

airplane_schema = StructType([
    StructField("airplane_id", IntegerType(), True),
    StructField("capacity", IntegerType(), True),
    StructField("type_id", IntegerType(), True),
    StructField("airline_id", IntegerType(), True)
])
