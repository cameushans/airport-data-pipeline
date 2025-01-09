from pyspark.sql.types import StructType, StructField, StringType, IntegerType, LongType

weather_data_schema = StructType([
    StructField("after", StructType([
        StructField("log_date", IntegerType(), True),
        StructField("time", IntegerType(), True),
        StructField("station", StringType(), True),
        StructField("temp", StringType(), True),
        StructField("humidity", StringType(), True),
        StructField("airpressure", IntegerType(), True),
        StructField("wind", StringType(), True),
        StructField("weather", StringType(), True),
        StructField("winddirection", StringType(), True)
    ]), True),
])
