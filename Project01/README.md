# Project1 - “Employment impact of COVID-19 in hotel occupancy, during the holy week in Mexico” 
## Date: June 2020
## Team
* Daniela Villarreal Murillo
* Michelle García Sanchez
* Juan Ramón Félix Alvarez Tostado
* Raúl Flores Palacios

## Hypothesis
With less arrivals of tourist during holy week of 2020 we estimate that at least there has been an impact of 50% on hotel occupation, that will translate to unemployment rate due to less demand .

## Facts
Relevant facts are:

* More the 9% Of the Mexican GDP is related to tourism
* OCDE countries are 4.7% average
* Tax Collection in Mexico is close to 14% of GDP. Tourism is almost equally important.

## Data Analytics process
The data analytics process we will follow on this exercise is illustrated on the following figure.
<Insert figure here>

## 1. Decompose the ask
THE ASK: How the employment in tourism in Mexico, during holy week 2020, was impacted by unpredicted events (COVID-19). From perception to real facts supported by data.
<Insert figure here>

## 2. Identify Data Sources
Data sources are listed here:
* [Datatour](https://www.datatur.sectur.gob.mx/SitePages/ResultadosITET.aspx) - Direct employments from the tourism sector in Mexico
* [Datatour](https://www.datatur.sectur.gob.mx/SitePages/ActividadHotelera.aspx) - Hotel activity in Mexico
* [OpenWeather](https://openweathermap.org/) - OpenWeather API
* [Google Maps](https://cloud.google.com/maps-platform/) - Google Maps Cloud Platform + API
* [GitHub](https://github.com/) - The version control software and repo

## 03. Define strategic metrics
Strategic Metrics we have defined for this exersice are:
* x% Occupation rate on the hospitality sector and airline airport arrivals as a reference per selected cities
* y% Time frame to be analyzed: 2018, 2019, 2020
* %Unemployment index impact on the hospitality sector by selected cities

## Lets go coding:
Now we will demonstrate on the Jupyter Notebook the following steps:
4. Plan data retrieval
5. Build data retrieval
6. Assemble and clean
7. Analyze trends

## 08. Recognize limitations
We have identified the following challenges during the execution of this exercise.
* Mexico lacks official data for strong analysis and updated data
* INEGI APIs are not user friendly
* Mexico local data does not match with international definitions

## 09. Tell the story
Relevant findings on the exercise are summarized here:

### Index Calculation
In order to have an employment index directly affected by the drop in tourist arrivals during the week, we took 3 factors: the proportion that represent the city at national level in room occupancy terms, the actual occupation of rooms during that period and the value of active employees during that period according to Sectur. Given that they are 3 indexes, we gave them the same weight by dividing them by 3. Then, to be able to compare the years 2019 and 2020, we take the proportion of falls from one to the other by dividing 2020 by 2019. 
So what all of this mean? At the end the index give us a proportion of the employment required to operate the hotel during this period which can help us to take in assumption that because the hotel is not operating in normal basis then they will need to reduce their collaborate teams to save in costs.

### Hotel Occupancy
* Based in the last 3 years we analyze how the occupancy has been.  
* Increase of 4% from 2018 to 2019.
* Decrease of 96% from 2019 to 2020
<Insert Image Here>

### Unemployment
* In the bar plot we present how unemployment affects each city in Mexico
* The cities with higher unemployment are: Puerto Escondido, Oaxaca, Cancun, Cozumel
<Insert Image Here>

### Airport Arrivals
* Based on the international flights we analyzed the decrease in tourism
* Decrease of 98% from 2019 to 2020
<Insert Image Here>

### Representation of unemployment impact
* A heatmap using google API has been used i order to represent economic impact
* Google API has been used also to represent locations
<Insert Image Here>
<Insert Image Here>
<Insert Image Here>

## Part II - Final Conclusions
### Challenges
* Mexico lacks official data for strong analysis and updated data
* INEGI APIs are not user friendly
* Mexico local data does not match with international definitions

### Approach
* We use tourism as our main source of analysis since it represents the 9% of economy
* We use hotel room occupation as an indirect method to calculate unemployment metrics
* We use top cities in the country as a representative sample of analysis

### Conclusions
* Top 5 cities impacted are: Puerto Escondido, Oaxaca, Cancún, Cozumel, Isla Mujeres
* The occupation rate drops 96% vs last year.
* The international arrivals drop to 98% on the holly week period.
* We estimate that 4.3M of direct employments were affected during holy week, partially or even totally.

### Learnings
* Data quality and data extraction is the top challenge
* Availability of data sources and correct data formats is a most
* Data cleansing is a first step process. If data cleansing is not done correctly, we are going to run into many errors


## Built With

* [Python](https://www.python.org/) - The development language used
* [Pandas](https://pandas.pydata.org/) - Oopen source data analysis and manipulation tool
* [OpenWeather](https://openweathermap.org/) - OpenWeather API
* [Google Maps](https://cloud.google.com/maps-platform/) - Google Maps Cloud Platform + API
* [GitHub](https://github.com/) - The version control software and repo


## Authors

* **Raúl Flores Palacios** - *Initial work* - [raulfloresp](https://github.com/raulfloresp/databootcamp)
* Daniela Villarreal Murillo
* Michelle García Sanchez
* Juan Ramón Félix Alvarez Tostado

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
