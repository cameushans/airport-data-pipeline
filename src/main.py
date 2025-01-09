from dotenv import load_dotenv
import os
from processing.batch.airplane.schema import airplane_schema
from processing.batch.airport_geo.schema import airport_geo_schema
from processing.batch.booking.schema import booking_schema
from processing.batch.shared.utils import create_session
from processing.batch.shared.utils import Extractor
from processing.batch.passenger.schema import passenger_schema
from processing.batch.passengerdetails.schema import passengerdetails_schema
from processing.batch.flightschedule.schema import flifght_schedule
from processing.batch.airport.schema import airport
from processing.batch.employee.schema import employee
from processing.batch.flight.schema import fligt_schema
from processing.batch.weatherdata.schema import weather_data_schema


load_dotenv()
    
kafka_bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
passenger_topic_name = os.getenv("PASSENGER_TOPIC_NAME")
booking_topic_name = os.getenv("BOOKING_TOPIC_NAME")
passenger_detail_topic_name = os.getenv("PASSENGER_DETAILS_TOPIC_NAME")
hdfs_uri = os.getenv("HDFS_URI")
warehouse = os.getenv("WAREHOUSE")
airline_topic_name = os.getenv('AIRLINE_TOPIC_NAME')
airplane_topic_name = os.getenv('AIRPLANE_TOPIC_NAME')
airplane_type_topic_name = os.getenv('AIRPLANE_TYPE_TOPIC_NAME')
airport_topic_name = os.getenv('AIRPORT_TOPIC_NAME')
airport_geo_topic_name = os.getenv('AIRPORT_GEO_TOPIC_NAME')
booking_topic_name = os.getenv('BOOKING_TOPIC_NAME')
employee_topic_name = os.getenv('EMPLOYEE_TOPIC_NAME')
flight_topic_name = os.getenv('FLIGHT_TOPIC_NAME')
flightschedule_topic_name = os.getenv('FLIGHTSCHEDULE_TOPIC_NAME')
passenger_topic_name = os.getenv('PASSENGER_TOPIC_NAME')
passenger_details_topic_name = os.getenv('PASSENGER_DETAILS_TOPIC_NAME')
weatherdata_topic_name = os.getenv('WEATHERDATA_TOPIC_NAME')

def main():
    spark = create_session.create_spark_session(hdfs_uri, warehouse)

    domain = {}

    domain[airplane_type_topic_name] = airplane_schema.airplane_schema
    domain[airport_topic_name] = airport.airport_info_schema
    domain[airport_geo_topic_name] = airport_geo_schema.airport_details_schema
    domain[booking_topic_name] = booking_schema.booking_schema
    domain[employee_topic_name] = employee.employee_schema
    domain[flight_topic_name] = fligt_schema.flight_schema
    domain[flightschedule_topic_name] = flifght_schedule.flight_schedule_schema
    domain[passenger_topic_name] = passenger_schema.passenger_schema
    domain[passenger_details_topic_name] = passengerdetails_schema.passenger_details_schema
    domain[weatherdata_topic_name] = weather_data_schema.weather_data_schema
    
    extracted_df = Extractor.extract(domain, spark, kafka_bootstrap_servers)
    
    for df in extracted_df: 
        df.show()
    

if __name__ == "__main__":
    main()
