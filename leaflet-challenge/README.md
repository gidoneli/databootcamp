# Leaflet Homework - Visualizing Data with Leaflet
## Date: September 2020
### By Raúl Flores Palacios

## INTRODUCTION 
Welcome to the United States Geological Survey, or USGS for short! The USGS is responsible for providing scientific data about natural hazards, the health of our ecosystems and environment; and the impacts of climate and land-use change. Their scientists develop new methods and tools to supply timely, relevant, and useful information about the Earth and its processes.

The USGS is interested in building a new set of tools that will allow them visualize their earthquake data. They collect a massive amount of data from all over the world each day, but they lack a meaningful way of displaying it. Their hope is that being able to visualize their data will allow them to better educate the public and other government organizations (and hopefully secure more funding..) on issues facing our planet.


## Level 1: Basic Visualization


### DATASET
The USGS provides earthquake data in a number of different formats, updated every 5 minutes. Visit the USGS GeoJSON Feed page and pick a data set to visualize. When you click on a data set, for example ‘All Earthquakes from the Past 7 Days’, you will be given a JSON representation of that data. You will be using the URL of this JSON to pull in the data for our visualization.

* The link to the DATASET is here:

https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php


For the purpose of this project, I selected the Summary of earthquates in the last month. The GEOJSON file is located here:

https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson


### VISUALIZATION
* Create a map using Leaflet that plots all of the earthquakes from your data set based on their longitude and latitude.
* Your data markers should reflect the magnitude of the earthquake in their size and color. Earthquakes with higher magnitudes should appear larger and darker in color.
* Include popups that provide additional information about the earthquake when a marker is clicked.
* Create a legend that will provide context for your map data.


My final visualization is illustrated here:



![alt text](https://github.com/raulfloresp/databootcamp/blob/master/D3-challenge/D3_data_journalism/images/final_chart.jpg?raw=true)



## Built With

* [Visual Studio Code](https://code.visualstudio.com/) - Source Code Editor
* [GitHub](https://github.com/) - The version control software and repo
* [D3 Library](https://d3js.org//) - D3 Driven Documents
* [Leaflet](https://leafletjs.com/) - an open-source JavaScript library for mobile-friendly interactive maps
* [MapBox](https://www.mapbox.com//) - An open source mapping platform for custom designed maps.


## Authors

* **Raúl Flores Palacios** - *Initial work* - [raulfloresp](https://github.com/raulfloresp/databootcamp)


## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
