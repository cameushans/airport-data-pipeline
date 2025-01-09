from pyspark.sql import SparkSession, DataFrame

def load_data(spark: SparkSession, domain: str, df: DataFrame):
    
    for key in domain.keys():
        df.createOrReplaceTempView(f"temp_{key}_table")
        
        spark.sql(f"""
        INSERT INTO airportdb.{key}
        SELECT * FROM temp_{key}_table
        """)    
