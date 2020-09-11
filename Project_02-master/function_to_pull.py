# Dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from census import Census

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Census API Key
from config2 import api_key
c = Census(api_key, year=2018)

POSTGRES = {
    'user': 'postgres',
    'pw': 'YOUR PASS',
    'db': 'project_02',
    'host': 'localhost',
    'port': '5432',
}
engine = create_engine('postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES)

def scrape ():
    
    #Defining Variables to Pull
    countries = pd.read_csv("CodesByCountry.csv")
    baseline = countries[['code ','country ']]
    baseline = baseline.drop_duplicates(subset=['country '],keep='first')
    baseline = baseline.dropna(subset=['country '])
    countries_list = baseline['code '].values.tolist()
    countries_list.append("B05006_001E")
    countries_list_name = baseline['country '].values.tolist()
    countries_list_name.append("TotalMigration")
    country_list = []
    for i in countries_list_name:
        a = str(i).replace(' ','')
        country_list.append(a)
        
    countries_list_name = country_list

    population = ["B01003_001E"]

    educational_degree_code = ["B06009_025E","B06009_026E","B06009_027E","B06009_028E","B06009_029E","B06009_030E"]
    educational_degree_name = ["TotalEducation","School","HighSchool","College","Bachelor","Graduate"]

    age_code = ["B06001_049E","B06001_050E","B06001_051E","B06001_052E","B06001_053E","B06001_055E",
                "B06001_056E","B06001_057E","B06001_058E","B06001_059E","B06001_060E"]
    age_name = ["TotalAge","age_5","age_18","age_25","age_35","age_45","age_55","age_60","age_65","age_75","age_75more"]

    income_code = ["B06010_045E","B06010_046E","B06010_047E","B06010_048E","B06010_049E","B06010_050E",
                "B06010_051E","B06010_052E","B06010_053E","B06010_054E","B06010_055E"]
    income_name = ["TotalIncome","NoIncome","Income","inc_10000","inc_15000","inc_25000","inc_35000",
                "inc_50000","inc_65000","inc_75000","inc_75000more"]

    sex_code = ["B06003_013E","B06003_014E","B06003_015E"]
    sex_name = ["TotalSex","Male","Female"]


    civil_status_code = ["B05007_001E","B05007_002E","B05007_003E","B05007_004E","B05007_005E","B05007_006E","B05007_007E",
                        "B05007_008E","B05007_009E","B05007_010E","B05007_011E","B05007_012E","B05007_013E"]
    civil_stats_name = ["TotalCivil","2010","NotCitizen2010","2010Citizen","2000","NotCitizen2000","2000Citizen",
                    "1990","NotCitizen1990","1990Citizen","lower1990","lower1990NotCitizen","lower1990Citizen"]
    
    #Creating String to Pull
    data = population + educational_degree_code + age_code + income_code + sex_code + civil_status_code
    data2 = educational_degree_name + age_name + income_name + sex_name + civil_stats_name

    key=data[0]
    for i in range(1,len(data)):
        key = key+","+data[i]
        
    key2=countries_list[0]
    for i in range(1,49):
        key2 = key2+","+countries_list[i]

    key3=countries_list[49]
    for i in range(50,98):
        key3 = key3+","+countries_list[i]

    key4=countries_list[98]
    for i in range(99,len(countries_list)):
        key4 = key4+","+countries_list[i]

    #Pull Data    
    census_data = c.acs5.get(("NAME", key), {'for': 'state:*'})
    census_data = pd.DataFrame(census_data)

    census_country1=c.acs5.get(("NAME", key2), {'for': 'state:*'})
    census_country1=pd.DataFrame(census_country1)
    census_country1 = census_country1.drop(columns=['NAME'])

    census_country2=c.acs5.get(("NAME", key3), {'for': 'state:*'})
    census_country2=pd.DataFrame(census_country2)
    census_country2 = census_country2.drop(columns=['NAME'])

    census_country3=c.acs5.get(("NAME", key4), {'for': 'state:*'})
    census_country3=pd.DataFrame(census_country3)
    census_country3 = census_country3.drop(columns=['NAME'])

    data_df = census_data.merge(census_country1,left_on="state",right_on="state")
    data_df = data_df.merge(census_country2,left_on="state",right_on="state")
    data_df = data_df.merge(census_country3,left_on="state",right_on="state")

    names_list = ["State_Name"]+["Population"]+educational_degree_name + age_name + income_name + sex_name + civil_stats_name+["State"]
    for x in countries_list_name:
        names_list.append(x)
    
    dic={}
    for i in range(0,len(data_df.columns)):
        dic[data_df.columns[i]]=names_list[i].lower()

    data_df = data_df.rename(columns= dic)
    data_df = data_df.set_index('state')
    data_df = data_df.fillna(0)

    data_df.to_sql(name='project', con=engine, if_exists='append', index=False)

    return data_df
