from pyspark.sql import DataFrame, SparkSession


def load(spark: SparkSession ,df: DataFrame, df_name: str) :
    df.createOrReplaceTempView("temp_{df_name}_table")
    
    spark.sql("""
    INSERT INTO airportdb.{df_name}
    SELECT * FROM temp_{df_name}_table
    """)  
            