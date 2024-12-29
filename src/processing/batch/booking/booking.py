from pyspark.sql import SparkSession, DataFrame
import pyspark.sql.functions as psf
from common.utils.baseclasse import Airport 

class Booking(Airport) :
    def __init__(self, schema, spark: SparkSession, kafka_bootstrap_servers: str, topic_name: str):
        super().__init__(schema, spark, kafka_bootstrap_servers, topic_name)
        self.schema = schema
        self.topic_name = topic_name
        
    def get_booking_df(self) -> DataFrame:
        try:
          kafka_df = self.spark.read \
            .format("kafka") \
            .option("kafka.bootstrap.servers", self.kafka_bootstrap_servers) \
            .option("subscribe", self.topic_name) \
            .option("startingOffsets", "earliest") \
            .option("auto.offset.reset", "latest")\
            .option("failOnDataLoss", "false")\
            .load()
            
          kafka = kafka_df.selectExpr("CAST(value AS STRING) as value").filter("value IS NOT NULL")


          d = kafka \
            .select(psf.get_json_object(kafka['value'],"$.payload").alias('payload')) \
            .select(psf.from_json(psf.col('payload'), self.schema).alias("data"))
     
          df = d.select(
            "data.after.booking_id", 
            "data.after.flight_id", 
            "data.after.seat", 
            "data.after.passenger_id",
            "data.after.price"
            )
    
          return df
        except Exception as e:
          print(f"Erreur détaillée: {str(e)}")
          raise