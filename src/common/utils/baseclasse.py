
from pyspark.sql import SparkSession, DataFrame

class Airport :
    def __init__(self, schema, spark: SparkSession, kafka_bootstrap_servers: str, topic_name: str):
        self.schema = schema
        self.spark = spark
        self.kafka_bootstrap_servers = kafka_bootstrap_servers
        self.topic_name = topic_name
