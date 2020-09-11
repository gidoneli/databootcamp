from flask import Flask, render_template, redirect, jsonify

import numpy as np
import pandas as pd
import requests
import json

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from sqlalchemy.orm import aliased


#################################################
# Database Setup
#################################################
POSTGRES = {
    'user': 'postgres',
    'pw': '@Pifarus_1190',
    'db': 'project_02',
    'host': 'localhost',
    'port': '5432',
}

engine = create_engine('postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Project = Base.classes.project

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/map/<country>/<age>/<education>/<income>")
def return_data(country,age,education,income):

    #Connect to data base
    session = Session(engine)

    country = country.replace(' ','').lower()
    education = education.replace(' ','').lower()
    if age == '+75':
        age = '75more'
    else:
        age = age[1::]
    if income == '+75000':
        income = '75more'
    else:
        income = income[1::]

    statement = f"SELECT {country},age_{age},inc_{income},{education} FROM project"

    results_var = engine.execute(statement).fetchall()

    fields = [Project.state_name,Project.population,Project.totaleducation,Project.totalage,Project.totalincome,Project.totalsex,Project.totalcivil,
    Project.notcitizen2010,Project.notcitizen2000,Project.notcitizen1990,Project.lower1990notcitizen,Project.totalmigration,Project.male]

   #Retrive data based on input
    results = session.query(*fields).all()

    all_data = []

    def safe_div(x,y):
        if y == 0:
            return 0
        return x / y

    for i in range(0,len(results)):
        data_dict = {}
        data_dict["state"] = results[i][0]
        data_dict["population"] = results[i][1]
        data_dict["education"] = safe_div(results_var[i][3],results[i][2])
        data_dict["age"] = safe_div(results_var[i][1],results[i][3])
        data_dict["income"] = safe_div(results_var[i][2],results[i][4])
        data_dict["status"] = 1-safe_div((results[i][7]+results[i][8]+results[i][9]+results[i][10]),results[i][6])
        data_dict["sex"] = safe_div(results[i][12],results[i][5])
        data_dict["variable"] = results_var[i][0]
        data_dict["migration"] = safe_div(results[i][11],results[i][1])
        data_dict["country_migration"] = safe_div(results_var[i][0],results[i][1])
        all_data.append(data_dict)
    
    session.close()
    dict_all_data={"data": all_data}

    return jsonify(dict_all_data)


if __name__ == "__main__":
    app.run(debug=True)
