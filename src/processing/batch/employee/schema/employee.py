from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DecimalType, DateType

employee_schema = StructType([
    StructField("before", StructType([
        StructField("employee_id", IntegerType(), True),
        StructField("firstname", StringType(), True),
        StructField("lastname", StringType(), True),
        StructField("birthdate", DateType(), True),
        StructField("sex", StringType(), True),
        StructField("street", StringType(), True),
        StructField("city", StringType(), True),
        StructField("zip", IntegerType(), True),
        StructField("country", StringType(), True),
        StructField("emailaddress", StringType(), True),
        StructField("telephoneno", StringType(), True),
        StructField("salary", DecimalType(10, 2), True),
        StructField("department", StringType(), True),
        StructField("username", StringType(), True),
        StructField("password", StringType(), True),
    ]), True)
])
