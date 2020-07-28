# Web Scraping Homework - Mission to Mars
## Date: July 2020
### By Raúl Flores Palacios


# Introduction
In this assignment, I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

# Step 1 - Scraping
* Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
* Create a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.

The Julyter Notebook can be located here:

https://github.com/raulfloresp/databootcamp/blob/master/web-scraping-challenge/Mission_to_mars.ipynb


## NASA Mars News
Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/web-scraping-challenge/images/Nasa_News.jpg?raw=true)


## JPL Mars Space Images - Featured Image
* Visit the url for JPL Featured Space Image here.
* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
* Make sure to find the image url to the full size .jpg image.
* Make sure to save a complete url string for this image.

Featured Imaged is illustrated bellow:

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/web-scraping-challenge/images/Featured_image.jpg?raw=true)



## Mars Weather
Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called mars_weather.
* Note: Be sure you are not signed in to twitter, or scraping may become more difficult.
* Note: Twitter frequently changes how information is presented on their website. If you are having difficulty getting the correct html tag data, consider researching Regular Expression Patterns and how they can be used in combination with the .find() method.

Results are illustrated bellow:

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/web-scraping-challenge/images/Weather_Jup.jpg?raw=true)


## Mars Facts
* Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
* Use Pandas to convert the data to a HTML table string.


Results are illustrated bellow:

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/web-scraping-challenge/images/Facts_notebook.jpg?raw=true)


## Mars Hemispheres
Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar’s hemispheres.
You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/web-scraping-challenge/images/Hemispheres_Notebook.jpg?raw=true)


# Step 2 - MongoDB and Flask Application
Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

The app.py file is located here:

https://github.com/raulfloresp/databootcamp/blob/master/web-scraping-challenge/app.py


The scrape_mars.py file is located here:

https://github.com/raulfloresp/databootcamp/blob/master/web-scraping-challenge/scrape_mars.py


The MongoDB database is illustrated here:

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/web-scraping-challenge/images/mongo.jpg?raw=true)


The HTML Template is illustrated here:

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/web-scraping-challenge/images/html01.jpg?raw=true)

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/web-scraping-challenge/images/Hemispheres.jpg?raw=true)



## Built With

* [Python](https://www.python.org/) - The development language used
* [Pandas](https://pandas.pydata.org/) - Oopen source data analysis and manipulation tool
* [Visual Studio Code](https://code.visualstudio.com/) - Source Code Editor
* [GitHub](https://github.com/) - The version control software and repo
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Web Development
* [MongoDB](https://www.mongodb.com/) - Database


## Authors

* **Raúl Flores Palacios** - *Initial work* - [raulfloresp](https://github.com/raulfloresp/databootcamp)


## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
