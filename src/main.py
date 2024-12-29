import pyspark.sql.functions as psf 
from dotenv import load_dotenv
import os
from common.utils import create_session
from processing.batch.passenger import passenger_schema
from processing.batch.passenger import passenger
from processing.batch.booking import booking
from processing.batch.booking import booking_schema
from processing.batch.passengerdetails import passengerdetails
from src.processing.batch.passengerdetails.schema import passengerdetails_schema
import polars as pl

def main():
    load_dotenv()

    
    kafka_bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
    passenger_topic_name = os.getenv("PASSENGER_TOPIC_NAME")
    booking_topic_name = os.getenv("BOOKING_TOPIC_NAME")
    passenger_detail_topic_name = os.getenv("PASSENGER_DETAILS_TOPIC_NAME")
    hdfs_uri = os.getenv("HDFS_URI")
    warehouse = os.getenv("WAREHOUSE")
    
    spark = create_session.create_spark_session(hdfs_uri, warehouse)

    traveler = passenger.Passenger(passenger_schema.passenger_schema, spark, kafka_bootstrap_servers, passenger_topic_name)
    df_passenger = traveler.get_passenger_df()
    
    df_passenger.createOrReplaceTempView("temp_passenger_table")
    
    spark.sql("""
    INSERT INTO airportdb.passenger
    SELECT * FROM temp_passenger_table
    """)  
            
if __name__ == "__main__":
    main()