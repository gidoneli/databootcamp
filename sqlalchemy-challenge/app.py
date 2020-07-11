# 1. Import Flask
# Python SQL toolkit and Object Relational Mapper
import numpy as np
import pandas as pd

import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import create_engine, inspect

from flask import Flask

#engine = create_engine("sqlite:///Resources/hawaii.sqlite")
engine = create_engine("sqlite:///hawaii.sqlite")


# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#Setup Flask
app = Flask(__name__)

#Global calculations
# Calculate the date 1 year ago from the last data point in the database
date_one_year = session.query(func.max(Measurement.date)).all()
final_date_one_year = date_one_year[0][0]
final_date = dt.datetime.strptime(final_date_one_year, "%Y-%m-%d")
begin_date = final_date - dt.timedelta(365)


# This function called `calc_temps` will accept start date and end date in the format '%Y-%m-%d' 
# and return the minimum, average, and maximum temperatures for that range of dates
def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVG, and TMAX
    """
    
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()





#FLASK ROUTES

# HOME
# List all routes that are available.
@app.route("/")
def main():
    """List all routes that are available."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

# PRECIPITATION: /api/v1.0/precipitation
# Convert the query results to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the JSON representation of your dictionary."""

    print("Received precipitation api request.")

    date_one_year = session.query(func.max(Measurement.date)).all()
    final_date_one_year = date_one_year[0][0]
    final_date = dt.datetime.strptime(final_date_one_year, "%Y-%m-%d")

    begin_date = final_date - dt.timedelta(365)

# Perform a query to retrieve the data and precipitation scores
    precipitation_data = session.query(func.strftime("%Y-%m-%d", Measurement.date), Measurement.prcp).\
        filter(func.strftime("%Y-%m-%d", Measurement.date) >= begin_date).all()
    precipitation_data

# Convert the query results to a dictionary using date as the key and prcp as the value.
    query_results_dict = {}
    for result in precipitation_data:
        query_results_dict[result[0]] = result[1]

# Return the JSON representation of your dictionary.
    return jsonify(query_results_dict)



# STATIONS
#/api/v1.0/stations
# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    stations = session.query(Station.name).all()
    stations_list = list(np.ravel(stations))
    return jsonify(stations_list)


# TEMPERATURE
#/api/v1.0/tobs
# Query the dates and temperature observations of the most active station for the last year of data.
# Return a JSON list of temperature observations (TOBS) for the previous year.
@app.route("/api/v1.0/temperature")
def temperature():

    active_stations = session.query(Measurement.station, func.count(Measurement.station)
                               ).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()

    results = (session.query(Measurement.date, Measurement.tobs, Measurement.station)
                      .filter(Measurement.date > begin_date)
                      .order_by(Measurement.date)
                      .all())

    temperature_data = []
    for active_station in active_stations:
        temp_dict = {active_station.date: active_station.tobs, "Station": active_station.station}
        temperature_data.append(temp_dict)

    return jsonify(temperature_data)



#/api/v1.0/<start> and /api/v1.0/<start>/<end>
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

#Start Date
@app.route("/api/v1.0/<start>")
def start(start):

    print("API REQUEST")

    #Prepare dates
    date_one_year = session.query(func.max(Measurement.date)).all()
    final_date_one_year = date_one_year[0][0]
    final_date = dt.datetime.strptime(final_date_one_year, "%Y-%m-%d")
    begin_date = final_date - dt.timedelta(365)
    
    #Temperatures
    temperatures = calc_temps(start, final_date)

    #create a list
    return_list = []
    date_dict = {'start_date': start, 'end_date': final_date}
    return_list.append(date_dict)
    return_list.append({'Measurement': 'TMIN', 'Temperature': temperatures[0][0]})
    return_list.append({'Measurement': 'TAVG', 'Temperature': temperatures[0][1]})
    return_list.append({'Measurement': 'TMAX', 'Temperature': temperatures[0][2]})

    return jsonify(return_list)

#When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    
    print("API REQUEST")

    #Temperatures
    temperatures = calc_temps(start, end)

    #create a list
    return_list = []
    date_dict = {'start_date': start, 'end_date': end}
    return_list.append(date_dict)
    return_list.append({'Observation': 'TMIN', 'Temperature': temperatures[0][0]})
    return_list.append({'Observation': 'TAVG', 'Temperature': temperatures[0][1]})
    return_list.append({'Observation': 'TMAX', 'Temperature': temperatures[0][2]})

    return jsonify(return_list)

if __name__ == '__main__':
    app.run(debug=True)
