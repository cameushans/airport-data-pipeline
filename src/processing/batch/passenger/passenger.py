from pyspark.sql import SparkSession, DataFrame
import pyspark.sql.functions as psf

from common.utils.baseclasse import Airport 


class Passenger(Airport):
    def __init__(self, schema, spark: SparkSession, kafka_bootstrap_servers: str, topic_name: str):
        super().__init__(schema, spark, kafka_bootstrap_servers, topic_name)
        self.schema = schema
        self.topic_name = topic_name
    def get_passenger_df(self) -> DataFrame:
    
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
            "data.after.passenger_id", 
            "data.after.passportno", 
            "data.after.firstname", 
            "data.after.lastname"
        )
        return df
    @staticmethod
    def count_passengers_with_firstname(df : DataFrame) -> int:
        df = df.filter(psf.col("firstname").isNotNull())
        print("The passenger total with first name is :", df.count())
    
    @staticmethod
    def count_total_passengers(df : DataFrame) -> int:
        df = df.select("passenger_id")
        print( "The passenger total is: ", df.count())
    
    @staticmethod
    def count_total_passengers_with_lastname(df : DataFrame) -> int:
        df = df.select("lastname")
        print("The total passenger with lastname provided is: ", df.count())
    
    @staticmethod
    def count_total_passengers_with_passportno(df : DataFrame) -> int:
        df = df.select("passportno")
        print("The total of passengers with passport provided is: ", df.count())
    
    @staticmethod
    def count_passengers_with_no_firstname(df : DataFrame) -> int:
        df = df.filter(psf.col("firstname").isNull())
        print("The total passenger with no firstname provided is: ", df.count())
    