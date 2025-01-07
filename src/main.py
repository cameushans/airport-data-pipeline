from dotenv import load_dotenv
import os
from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from src.processing.batch.airplane.schema import airplane_schema
from src.processing.batch.airline.schema import airline_type_schema
from src.processing.batch.airplane.schema import airplane_schema
from src.processing.batch.airport_geo.schema import airport_geo_schema
from src.processing.batch.booking.schema import booking_schema
from src.processing.batch.shared.utils import create_session
from src.processing.batch.shared.utils import Extractor
from src.processing.batch.passenger.schema import passenger_schema
from src.processing.batch.passengerdetails.schema import passengerdetails_schema
from src.processing.batch.flightschedule.schema import flifght_schedule
from src.processing.batch.airport.schema import airport
from src.processing.batch.employee.schema import employee
from src.processing.batch.flight.schema import fligt_schema
from src.processing.batch.shared.utils.Loader import load, load_data
from src.processing.batch.shared.utils.extract_column import extract_fields
from src.processing.batch.weatherdata.schema import weather_data_schema

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

    dag = DAG(
        'simple_dag',
        description='A simple DAG',
        schedule_interval=timedelta(days=1),
        start_date = days_ago(1),
    )
    
    domain = {}

    domain[airline_topic_name] = airline_type_schema
    domain[airplane_topic_name] = airplane_schema
    domain[airplane_type_topic_name] = airplane_schema
    domain[airport_topic_name] = airport
    domain[airport_geo_topic_name] = airport_geo_schema
    domain[booking_topic_name] = booking_schema
    domain[employee_topic_name] = employee
    domain[flight_topic_name] = fligt_schema
    domain[flightschedule_topic_name] = flifght_schedule
    domain[passenger_topic_name] = passenger_schema
    domain[passenger_details_topic_name] = passengerdetails_schema
    domain[weatherdata_topic_name] = weather_data_schema

    
    
    
    t1 = PythonOperator(
        task_id='Extract_From_Kafka',
        python_callable=Extractor.extract(domain, extract_fields, spark, kafka_bootstrap_servers),
        depends_on_past=False,
        dag=dag,
    )
    
    t2 = PythonOperator(
        task_id='Load_data_to_iceberg',
        depends_on_past=True,
        python_callable=load(ti),
        dag=dag,
    )
     
    t1 >> t2
            
if __name__ == "__main__":
    main()
    