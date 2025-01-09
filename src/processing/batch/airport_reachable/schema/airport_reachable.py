from pyspark.sql.types import StructType, StructField, IntegerType

airport_reachable_schema = StructType([
    StructField("after", StructType([
        StructField("airport_id", IntegerType(), True),
        StructField("hops", IntegerType(), True)
    ]), True)
])
