from pyspark.sql import SparkSession
def create_spark_session() -> SparkSession :
    spark = SparkSession.builder \
        .appName("KafkaBatchProcessing") \
        .config("spark.hadoop.fs.defaultFS", "hdfs://192.168.1.94:9000") \
        .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkCatalog") \
        .config("spark.sql.catalog.spark_catalog.type", "hadoop") \
        .config("spark.sql.catalog.spark_catalog.warehouse", "hdfs://192.168.1.94:9000/iceberg_warehouse") \
        .getOrCreate()
        
    spark.sql("CREATE DATABASE IF NOT EXISTS airportdb")
    
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.airplane (
        airplane_id INT,
        capacity INT,
        type_id INT,
        airline_id INT
        )  USING iceberg
    """)
    
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.passenger (
        passenger_id INT,
        passportno STRING,
        firstname STRING,
        lastname STRING
    ) USING iceberg
    """)

    

    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.passengerdetails (
        passenger_id INT,
        birthdate STRING,
        sex STRING,
        street STRING,
        city STRING,
        zip INT,
        country STRING,
        emailadress STRING,
        telephoneno STRING
    ) USING iceberg
    """)
    
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.employee (
        employee_id INT,
        firstname STRING,
        lastname STRING,
        birthdate DATE,
        sex STRING,
        street STRING,
        city STRING,
        zip INT,
        country STRING,
        emailaddress STRING,
        telephoneno STRING,
        salary DECIMAL(10, 2),
        department STRING,
        username STRING,
        password STRING
    ) USING iceberg
    """)
    
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.weatherdata (
    log_date DATE,
    time TIMESTAMP,  -- Remplacer TIME par TIMESTAMP
    station INTEGER,
    temp DECIMAL(5, 2),
    humidity DECIMAL(5, 2),
    airpressure DECIMAL(10, 2),
    wind DECIMAL(5, 2),
    weather STRING,
    winddirection STRING
    ) USING iceberg;
    """)
    
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.airport (
        airport_id INT,
        iata STRING,
        icao STRING,
        name STRING
    ) USING iceberg
    """)


    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.airport_reachable (
        airport_id INT,
        hops INT
    ) USING iceberg
    """)
    
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.booking (
        booking_id INT,
        flight_id INT,
        seat STRING,
        passenger_id INT,
        price DECIMAL(10, 2)
    ) USING iceberg
    """)
    
    
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.airport_geo (
        airport_id INT,
        name STRING,
        city STRING,
        country STRING,
        latitude DECIMAL(11, 8),
        longitude DECIMAL(11, 8),
        geolocation STRING
    ) USING iceberg
    """)
    
    
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.flight (
        flight_id INT,
        flightno STRING,
        `from` INT,
        `to` INT,
        departure TIMESTAMP,
        arrival TIMESTAMP,
        airline_id INT,
        airplane_id INT
    ) USING iceberg
    """)
    
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.flightschedule (
        flightno STRING,
        from INT,
        to INT,
        departure STRING,
        arrival STRING,
        airline_id INT,
        monday BOOLEAN,
        tuesday BOOLEAN,
        wednesday BOOLEAN,
        thursday BOOLEAN,
        friday BOOLEAN,
        saturday BOOLEAN,
        sunday BOOLEAN
    ) USING iceberg
    """)
    
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.airline (
        airline_id INT,
        iata STRING,
        airlinename STRING,
        base_airport INT
    ) USING iceberg
   """)
    
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.airplane_type (
        type_id INT,
        identifier STRING,
        description STRING
    ) USING iceberg
    """)
    
    spark.sql("""
    CREATE TABLE IF NOT EXISTS airportdb.flight_log (
    flight_log_id BIGINT,
    log_date TIMESTAMP,
    user STRING,
    flight_id INT,
    flightno_old STRING,
    flightno_new STRING,
    from_old INT,
    to_old INT,
    from_new INT,
    to_new INT,
    departure_old TIMESTAMP,
    arrival_old TIMESTAMP,
    departure_new TIMESTAMP,
    arrival_new TIMESTAMP,
    airplane_id_old INT,
    airplane_id_new INT,
    airline_id_old INT,
    airline_id_new INT,
    comment STRING
  ) USING iceberg
  """)






    return spark    


                