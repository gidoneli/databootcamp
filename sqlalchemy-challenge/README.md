# Homework3: SQLAlchemy Homework - Surfs Up!
## Date: July 2020
### By Raúl Flores Palacios


## Step 1A - Precipitation Analysis and Exploration: 
Use Python and SQLAlchemy to do basic climate analysis and data exploration of a climate database. All of the following analysis were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Query to retrieve the last 12 months of precipitation data and plot the results: 19550


* Select only the date and prcp values.
![alt text](https://github.com/raulfloresp/databootcamp/blob/master/sqlalchemy-challenge/images/Plot00.jpg?raw=true)


* Load the query results into a Pandas DataFrame and set the index to the date column.

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/sqlalchemy-challenge/images/Plot_Pandas.jpg?raw=true)


* Sort the DataFrame values by date.

* Plot the results using the DataFrame plot method.

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/sqlalchemy-challenge/images/Plot01.png?raw=true)


* Use Pandas to print the summary statistics for the precipitation data.

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/sqlalchemy-challenge/images/Statistics.jpg?raw=true)


## Step 1B - Station Analysis and Exploration: 
Use Python and SQLAlchemy to do basic climate analysis and data exploration of a climate database. All of the following analysis were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* List of stations

['WAIKIKI 717.2, HI US',
 'KANEOHE 838.1, HI US',
 'KUALOA RANCH HEADQUARTERS 886.9, HI US',
 'PEARL CITY, HI US',
 'UPPER WAHIAWA 874.3, HI US',
 'WAIMANALO EXPERIMENTAL FARM, HI US',
 'WAIHEE 837.5, HI US',
 'HONOLULU OBSERVATORY 702.2, HI US',
 'MANOA LYON ARBO 785.2, HI US']


* Design a query to calculate the total number of stations: 
* Design a query to find the most active stations.

[('USC00519281', 2772),
 ('USC00519397', 2724),
 ('USC00513117', 2709),
 ('USC00519523', 2669),
 ('USC00516128', 2612),
 ('USC00514830', 2202),
 ('USC00511918', 1979),
 ('USC00517948', 1372),
 ('USC00518838', 511)]

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/sqlalchemy-challenge/images/Active%20stations.jpg?raw=true)


* List the stations and observation counts in descending order.
* Which station has the highest number of observations?
* Design a query to retrieve the last 12 months of temperature observation data (TOBS).
* Filter by the station with the highest number of observations.
* Plot the results as a histogram with bins=12.

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/sqlalchemy-challenge/images/Plot02.png?raw=true)


## Step 2 - Climate App
After initial analysis, design a Flask API based on the queries developed.
Use Flask to create your routes.

Routes:
* /Home page.
* /api/v1.0/precipitation
* /api/v1.0/stations
* /api/v1.0/tobs
* /api/v1.0/<start> and /api/v1.0/<start>/<end>

Refer to the APP.PY File here: 
![alt text](https://github.com/raulfloresp/databootcamp/blob/master/Project01/Images/Tourism_Economy.png?raw=true)


## BONUS
calculate the tmin, tavg, and tmax 
[(70.0, 78.32352941176471, 85.0)]

Temperature Observations
![alt text](https://github.com/raulfloresp/databootcamp/blob/master/sqlalchemy-challenge/images/Temperature%20Observations.jpg?raw=true)


### Plot the results from your previous query as a bar chart. 
![alt text](https://github.com/raulfloresp/databootcamp/blob/master/sqlalchemy-challenge/images/Plot%20Bar.png?raw=true)


## Built With

* [Python](https://www.python.org/) - The development language used
* [Pandas](https://pandas.pydata.org/) - Oopen source data analysis and manipulation tool
* [Visual Studio Code](https://code.visualstudio.com/) - Source Code Editor
* [GitHub](https://github.com/) - The version control software and repo
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Web App


## Authors

* **Raúl Flores Palacios** - *Initial work* - [raulfloresp](https://github.com/raulfloresp/databootcamp)


## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
