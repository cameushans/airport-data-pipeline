from typing import Any, Dict
from pyspark import SparkSession, DataFrame
from pyspark.sql import SparkSession, DataFrame
import pyspark.sql.functions as psf


class Extract():
    def __init__(self, schema, spark: SparkSession, kafka_bootstrap_servers: str, topic_name: str, fields: str ):
        super().__init__(schema, spark, kafka_bootstrap_servers, topic_name)
        self.schema = schema
        self.topic_name = topic_name
        self.fields = fields
        self.kafka_bootstrap_servers = kafka_bootstrap_servers
        
    def get_df(self) -> DataFrame:
    
        kafka_df = self.spark.read \
        .format("kafka") \
        .option("kafka.bootstrap.servers", self.kafka_bootstrap_servers) \
        .option("subscribePattern", self.topic_name) \
        .option("startingOffsets", "earliest") \
        .load() \
            
        kafka = kafka_df.selectExpr("CAST(value AS STRING) as value").filter("value IS NOT NULL")

        d = kafka \
            .select(psf.get_json_object(kafka['value'],"$.payload").alias('payload')) \
            .select(psf.from_json(psf.col('payload'), self.schema).alias("data")) \

        df = d.select(
            *[f"data.value.{item}" for item in self.fields]
        )
        
        return df
    
def extract(domain: Dict, extract_fields: function,  spark: SparkSession, kafka_bootstrap_servers: Any):
    dfs = []
    for topic_name, schema, field in domain.keys(), domain.values(), extract_fields(domain.values()):
            dfs.append(Extract(schema, spark, kafka_bootstrap_servers, topic_name, field).get_df())
            return dfs