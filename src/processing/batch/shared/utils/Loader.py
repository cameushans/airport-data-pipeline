from typing import List
from annotated_types import T
from pyspark.sql import SparkSession, DataFrame

def load_data(spark: SparkSession, df: List[T]):
    for df in df:
        df.createOrReplaceTempView(f"temp_{domain}_table")
        
        spark.sql(f"""
        INSERT INTO airportdb.{domain}
        SELECT * FROM temp_{domain}_table
        """)
        
        
def load(ti: any):
        input_data = ti.xcom_pull(task_ids="Extract_From_Kafka")
        load_data(input_data)        
