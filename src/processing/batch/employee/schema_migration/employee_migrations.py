from pyspark.sql import SparkSession

def apply_employee_migrations(spark: SparkSession):
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.employee (
        employee_id INT,
        firstname STRING,
        lastname STRING,
        birthdate DATE,
        sex STRING,
        street STRING,
        city STRING,
        zip INT,
        country STRING,
        emailaddress STRING,
        telephoneno STRING,
        salary DECIMAL(10, 2),
        department STRING,
        username STRING,
        password STRING
    ) USING iceberg
    """)