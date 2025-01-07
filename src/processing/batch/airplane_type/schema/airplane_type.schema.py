from pyspark.sql.types import StructType, StructField, StringType, IntegerType

airport_type_schema = StructType([
    StructField("type_id", IntegerType(), True),
    StructField("identifier", StringType(), True),
    StructField("description", StringType(), True)
])