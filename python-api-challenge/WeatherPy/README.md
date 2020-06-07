# Python API Homework - What’s the Weather Like?
### Python_API_Challenge

Homework 6 - Python API Homework - What’s the Weather Like?
By Raúl Flores / @raulfloresp

## Part I - WeatherPy
Create a Python script to visualize the weather of 500+ cities across the world of varying distance from the equator. 
First requirement is to create a series of scatter plots to showcase the following relationships:

* Temperature (F) vs. Latitude
* Humidity (%) vs. Latitude
* Cloudiness (%) vs. Latitude
* Wind Speed (mph) vs. Latitude
* After each plot add a sentence or too explaining what the code is and analyzing.

Second requirement is to run linear regression on each relationship, only this time separating them into Northern Hemisphere (greater than or equal to 0 degrees latitude) and Southern Hemisphere (less than 0 degrees latitude):

* Northern Hemisphere - Temperature (F) vs. Latitude
* Southern Hemisphere - Temperature (F) vs. Latitude
* Northern Hemisphere - Humidity (%) vs. Latitude
* Southern Hemisphere - Humidity (%) vs. Latitude
* Northern Hemisphere - Cloudiness (%) vs. Latitude
* Southern Hemisphere - Cloudiness (%) vs. Latitude
* Northern Hemisphere - Wind Speed (mph) vs. Latitude
* Southern Hemisphere - Wind Speed (mph) vs. Latitude

### Results: Latitude vs. Temperature Plot
A scatter plot is a type of a mathematical diagram using Cartesian coordinates to display values for typically two variables for a set of data. The data are displayed as a collection of points, each having the value of one variable determining the position on the horizontal axis and the value of the other variable determining the position on the vertical axis.
A scatter plot can be used either when one continuous variable that is under the control of the experimenter and the other depends on it. In this case we are analyzing how the Temperature behaves along the Latitude of cities.
The measured or dependent variable is customarily plotted along the vertical axis, that is the case of Temperature. The scatter plot can suggest various kinds of correlations between variables with a certain confidence interval.
We can see that Temperature on the low and high values of Latitude is cold. That is an expected behavior, because those cities are close to the poles. Cities at the center of the earth are quite warm and hot and it is also demonstrated on the scatter plot.

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/python-api-challenge/WeatherPy/Latitude_vs_Temperature.png?raw=true)

### Results: Latitude vs. Humidity Plot
The measured or dependent variable is customarily plotted along the vertical axis, that is the case of Humidity. The scatter plot can suggest various kinds of correlations between variables with a certain confidence interval.
We can see some kind of correlation between these two variables. Humidity is more correlated in cities with Latitude above 0, so it increases when we move to cities with Latitude between 60 to 80.

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/python-api-challenge/WeatherPy/Latitude_vs_Humidity.png?raw=true)

### Results: Latitude vs. Cloudiness Plot
The measured or dependent variable is customarily plotted along the vertical axis, that is the case of Clodiness. The scatter plot can suggest various kinds of correlations between variables with a certain confidence interval.
We can not appreciate a clear correlation between two variables bacuase all the points are spread along the graph.
![alt text](https://github.com/raulfloresp/databootcamp/blob/master/python-api-challenge/WeatherPy/Latitude_vs_Cloudiness.png?raw=true)

### Results: Latitude vs. Wind Speed Plot
The measured or dependent variable is customarily plotted along the vertical axis, that is the case of Wind Speed. The scatter plot can suggest various kinds of correlations between variables with a certain confidence interval.
We can not appreciate a clear correlation between two variables bacuase all the points are spread along the graph.
![alt text](https://github.com/raulfloresp/databootcamp/blob/master/python-api-challenge/WeatherPy/Latitude_vs_WindSpeed.png?raw=true)


### LINEAR REGRESSION
### 1. Northern Hemisphere - Max Temp vs. Latitude Linear Regression¶
Linear regression has a r-squared value of -0.75. There is a medium to hight negative linear relation between latitude and temperature when both are descreasing in the Northern Hemisphere. We can observe that 75% of the variance is explained by this linear model.

### 2. Southern Hemisphere - Max Temp vs. Latitude Linear Regression
Linear regression has a r-squared value of -0.81. There is a hight linear relation between latitude and temperature when both are increasing in the Southern Hemisphere. We can observe that 81% of the variance is explained by this linear model - strong correlation.

### 3. Northern Hemisphere - Humidity (%) vs. Latitude Linear Regression
Linear regression has a r-squared value of -0.81. There is a hight linear relation between latitude and temperature when both are increasing in the Southern Hemisphere. We can observe that 81% of the variance is explained by this linear model - strong correlation.

### 4. Southern Hemisphere - Humidity (%) vs. Latitude Linear Regression
Linear regression has a r-squared value of -0.067. There is a minimum linear relation between latitude and humidity when both are increasing in the Southern Hemisphere. We can observe that 6.79% of the variance is explained by this linear model - minimum correlation.

### 5. Northern Hemisphere - Cloudiness (%) vs. Latitude Linear Regression
Linear regression has a r-squared value of -0.1186. There is a weak linear relation between latitude and Cloudiness when both are increasing in the Northern Hemisphere. We can observe that 11.86% of the variance is explained by this linear model - weak correlation.

### 6. Southern Hemisphere - Cloudiness (%) vs. Latitude Linear Regression
Linear regression has a r-squared value of -0.026. There is a minimum linear relation between latitude and Cloudiness when both are increasing in the Southern Hemisphere. We can observe that 2.61% of the variance is explained by this linear model - minimum correlation.

### 7. Northern Hemisphere - Wind Speed (mph) vs. Latitude Linear Regression
Linear regression has a r-squared value of -0.028. There is a minimum linear relation between latitude and wind speed when both are increasing in the Northern Hemisphere. We can observe that 2.8% of the variance is explained by this linear model - almost no correlation exist.

### 8. Southern Hemisphere - Wind Speed (mph) vs. Latitude Linear Regression
Linear regression has a r-squared value of -0.135. There is a minimum linear relation between latitude and wind speed when both are increasing in the Southern Hemisphere. We can observe that 13.5% of the variance is explained by this linear model - Minimym correlation is appreciated.


## Part II - VacationPy¶
Plan future vacations - Use jupyter-gmaps and the Google Places API for this part of the assignment.

Create a heat map that displays the humidity for every city from the part I of the homework.


Narrow down the DataFrame to find your ideal weather condition. For example:
* A max temperature lower than 80 degrees but higher than 70.
* Wind speed less than 10 mph.
* Zero cloudiness.
* Drop any rows that don’t contain all three conditions. You want to be sure the weather is ideal.


## Built With

* [Python](https://www.python.org/) - The development language used
* [Pandas](https://pandas.pydata.org/) - Oopen source data analysis and manipulation tool
* [OpenWeather](https://openweathermap.org/) - OpenWeather API
* [Google Maps](https://cloud.google.com/maps-platform/) - Google Maps Cloud Platform + API
* [GitHub](https://github.com/) - The version control software and repo


## Authors

* **Raúl Flores Palacios** - *Initial work* - [raulfloresp](https://github.com/raulfloresp/databootcamp)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
