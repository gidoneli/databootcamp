# Web Design Homework - Web Visualization Dashboard (Latitude)
## Date: July 2020
### By Raúl Flores Palacios


## Introduction
For this homework I created a visualization dashboard website using visualizations I’ve created in a past assignment - "python-api-challenge". Specifically, I’ll be plotting weather data.

In building this dashboard, I created individual pages for each plot and a means by which you can navigate between them. These pages will contain the visualizations and their corresponding explanations. There is a landing page, a page where you can see a comparison of all of the plots, and another page where you can view the data I used to build them.

Web Pages created are:

## Landing Page
* An explanation of the project.
* Links to each visualizations page. There should be a sidebar containing preview images of each plot, and clicking an image should take the user to that visualization.

https://github.com/raulfloresp/databootcamp/blob/master/Web-Design-Challenge/WebVisualizations/index.html

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/Web-Design-Challenge/WebVisualizations/Assets/Landing_Page.jpg?raw=true)


## Visualizations Pages
    a) Temperature
    b) Humidity
    c) Cloudiness
    d) Wind Speed

These visualizations include:
* A descriptive title and heading tag.
* The plot/visualization itself for the selected comparison.
* A paragraph describing the plot and its significance.

https://github.com/raulfloresp/databootcamp/blob/master/Web-Design-Challenge/WebVisualizations/visual01.html

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/Web-Design-Challenge/WebVisualizations/Assets/Visualizations_Page.jpg?raw=true)


## A comparisons page
Contains all of the visualizations on the same page so we can easily visually compare them.
* Uses a Bootstrap grid for the visualizations.
* The grid must be two visualizations across on screens medium and larger, and 1 across on extra-small and small screens.

https://github.com/raulfloresp/databootcamp/blob/master/Web-Design-Challenge/WebVisualizations/comparison.html

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/Web-Design-Challenge/WebVisualizations/Assets/Comparisons.jpg?raw=true)


## A Data page
Displays a responsive table containing the data used in the visualizations.
* The table must be a bootstrap table component.
* The data must come from exporting the .csv file as HTML, or converting it to HTML.

https://github.com/raulfloresp/databootcamp/blob/master/Web-Design-Challenge/WebVisualizations/data.html

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/Web-Design-Challenge/WebVisualizations/Assets/Data.jpg?raw=true)


## Main design considerations
The website must, at the top of every page, have a navigation menu that:

* Has the name of the site on the left of the nav which allows users to return to the landing page from any page.
* Contains a dropdown menu on the right of the navbar named “Plots” that provides a link to each individual visualization page.
* Provides two more text links on the right: “Comparisons,” which links to the comparisons page, and “Data,” which links to the data page.
* Is responsive (using media queries). The nav must have similar behavior as the screenshots “Navigation Menu” section (notice the background color change).


![alt text](https://github.com/raulfloresp/databootcamp/blob/master/Web-Design-Challenge/WebVisualizations/Assets/Nav_Bar.jpg?raw=true)



## Built With

* [Python](https://www.python.org/) - The development language used
* [Pandas](https://pandas.pydata.org/) - Oopen source data analysis and manipulation tool
* [Visual Studio Code](https://code.visualstudio.com/) - Source Code Editor
* [GitHub](https://github.com/) - The version control software and repo
* [Bootstrap](https://getbootstrap.com/) - Web Framework


## Authors

* **Raúl Flores Palacios** - *Initial work* - [raulfloresp](https://github.com/raulfloresp/databootcamp)


## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
