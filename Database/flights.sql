-- Create table flights
-- Import data from csv file into created table
CREATE TABLE flights (
    year SMALLINT NOT NULL,
    month SMALLINT NOT NULL,
    day SMALLINT NOT NULL,
    day_of_week SMALLINT NOT NULL,
    airline VARCHAR(2) NOT NULL,
    flight_number SMALLINT NOT NULL,
    tail_number VARCHAR(6),
    origin_airport VARCHAR(5) NOT NULL,
    destination_airport VARCHAR(5) NOT NULL,
    scheduled_departure SMALLINT NOT NULL,
    departure_time SMALLINT,
    departure_delay SMALLINT,
    taxi_out SMALLINT,
    wheels_off SMALLINT,
    scheduled_time SMALLINT,
    elapsed_time SMALLINT,
    air_time SMALLINT,
    distance SMALLINT,
    wheels_on SMALLINT,
    taxi_in SMALLINT,
    scheduled_arrival SMALLINT,
    arrival_time SMALLINT,
    arrival_delay SMALLINT,
    diverted SMALLINT,
    cancelled SMALLINT NOT NULL,
    cancellation_reason VARCHAR(1),
    air_system_delay SMALLINT,
    security_delay SMALLINT,
    airline_delay SMALLINT,
    late_aircraft_delay SMALLINT,
    weather_delay SMALLINT
);

-- Create unique identifiers for each instance/row
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

alter table flights
	ADD COLUMN flight_id uuid DEFAULT uuid_generate_v4 ();

-- Make unique identifier primary key
ALTER TABLE flights
    ADD PRIMARY KEY (flight_id);

-- Create table airlines
-- Import data from csv file into created table
CREATE TABLE airlines (
    iata_code VARCHAR(2) NOT NULL,
    airline VARCHAR(30) NOT NULL,
    PRIMARY KEY (iata_code)
);

-- Create table airports
-- Import data from csv file into created table
CREATE TABLE airports (
    iata_code VARCHAR(3) NOT NULL,
    airport VARCHAR(80) NOT NULL,
    city VARCHAR(35) NOT NULL,
    state VARCHAR(2) NOT NULL,
    country VARCHAR(3) NOT NULL,
    latitude DECIMAL,
    longitude DECIMAL,
    PRIMARY KEY (iata_code)
);
