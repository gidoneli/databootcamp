# PROJECT 2
## Date: Agosto 2020
### By Raúl Flores Palacios


## A BRIEF ARTICULATION OF YOUR CHOSEN TOPIC AND RATIONALE. 
Immigrants consist of almost 14% of the USA population. For this project we will analyze the main countries of origin for this immigrants and the most popular cities for destination. We will review variables that will give us more information on the group of people living in the main states.

For these projects we will use the following sources: 
United States Census Bureu: https://www.census.gov/data/tables/time-series/demo/geographic-mobility/historic.html.  This database contains all the information from USA about economy and people. For this specific project we use the immigrants information. They report information per state , or per birth country; as well as economic , education & status variables. 

The Immigration Center: https://www.ilctr.org/quick-us-immigration-statistics/?gclid=EAIaIQobChMI-Yersuud6wIVB9bACh219wicEAAYAiAAEgKNufD_BwE. This database provides relevant information on immigration along with stadistics.


## 3 OR 4 SCREENSHOTS OF RELEVANT, “INSPIRING” VISUALIZATIONS THAT FRAME YOUR CREATIVE FODDER.
The inspiration is llustrated here:

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/Project_02-master/images/image01.jpg?raw=true)


## A SKETCH OF THE FINAL DESIGN
Refer to the following design:

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/Project_02-master/images/image02.jpg?raw=true)


## LINK TO GITHUB PAGE:
https://github.com/raulfloresp/databootcamp/tree/master/Project_02-master




# FINAL PROJECT RESULTS

## OBJECTIVES
* Overview of USA Migration from Latin America countries. 
* Locate the most popular cities for residence.
* Review variables that give us more insights on the status and group of people per state.   


## RESEARCH PROCESS
Define the scope of the analysis: 
* How immigrants behave on each of the states.
* Demographic analysis. 
* Focus on LatinAmerican countries. 


Identify data sources: 
* US Census
* Migration Policy Institute
* The Immigration Center
* BEA


* Identify the tool frameworks and resources to create the storytelling. 
* D3 Gallery.
* Mapbox.
* Plotly.
* AOS library (NEW). 



## ETL PROCESS
EXTRACT: 
* United States Census : We use this database for getting the information on country of origin, number of immigrants per state, age, income, and other economic variables. Source of information :https://www.census.gov/data/tables/time-series/demo/geographic-mobility/historic.html. 


TRANSFORM:
* On Jupyter Notebook - Filter codes for country and state to create a data frame with all the data. 
* Matrix with percentage of immigrants on each country and state.
* Json file with immigrant numbers per state and country for scatter plot. 


LOAD: 
* Postgres loading: SQL structure.
* Load from Pandas to Postgres. 


## FRONT-END AND BACK-END
The final result on the front-end is illustrated here:

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/Project_02-master/images/image02.jpg?raw=true)



## CONCLUSIONS
* Central American immigration is greater than South America. 
* Mexico is an outlier compare to Latin countries. 
* Caribbean islands tend to migrate to the East Coast. 
* Central American migrants are more attractive to USA Hispanic origin states.  
* Mexico & El Salvador are the top countries of birth from immigrants.
* California, Florida & Texas are the most popular states. 



## LEARNINGS
* Consolidation into a final endpoint takes time and complexity on merge. 
* User interface and frontend is a complete project. 
* ETL process is the biggest challenge. 
* Deployment and production is an extra challenge. 



## Built With

* [Visual Studio Code](https://code.visualstudio.com/) - Source Code Editor
* [GitHub](https://github.com/) - The version control software and repo
* [Bootstrap](https://getbootstrap.com/) - Javascript Framework
* [PostgreSQL](https://www.postgresql.org/) - Database
* [Leaflet](https://leafletjs.com/) - Interactive Maps
* [Javascript](https://www.javascript.com/) - Programing Language


## Authors

* **Raúl Flores Palacios** - *Initial work* - [raulfloresp](https://github.com/raulfloresp/databootcamp)


## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
