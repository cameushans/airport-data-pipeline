from typing import Any, Dict
import pyspark.sql.functions as psf
from pyspark.sql.types import StructType,StructField



class Extract():
    def __init__(self, schema, spark, kafka_bootstrap_servers: str, topic_name: str, fields):
        self.spark = spark  # SparkSession instance
        self.schema = schema
        self.topic_name = topic_name
        self.fields = fields
        self.kafka_bootstrap_servers = kafka_bootstrap_servers
        
    def get_df(self):
    
        kafka_df = self.spark.read \
        .format("kafka") \
        .option("kafka.bootstrap.servers", self.kafka_bootstrap_servers) \
        .option("subscribePattern", self.topic_name) \
        .option("startingOffsets", "earliest") \
        .load() \
            
        kafka = kafka_df.selectExpr("CAST(value AS STRING) as value")

        d = kafka \
            .select(psf.get_json_object(kafka['value'],"$.payload").alias('payload')) \
            .select(psf.from_json(psf.col('payload'), self.schema).alias("data")) \
                
        df = d.selectExpr(*[f"data.after.{item}" for item in self.fields])
        
        return df 

    
def extract(domain, spark, kafka_bootstrap_servers):
    dfs = {}
    for topic_name, schema in zip(domain.keys(), domain.values()):
       d =  Extract(schema, spark, kafka_bootstrap_servers, topic_name, extract_fields(schema))
       dfs[topic_name] = d.get_df()

    return dfs 

def extract_fields(schema):
    fields = []

    if isinstance(schema, StructType):
        for field in schema.fields:  # On itère sur les champs du StructType
            # Si le champ n'est pas un StructType imbriqué, on ajoute le nom du champ à la liste
            if not isinstance(field.dataType, StructType):
                fields.append(field.name)
            else:
                # Si c'est un StructType, on appelle récursivement pour extraire les champs à l'intérieur
                fields.extend(extract_fields(field.dataType))

    return fields