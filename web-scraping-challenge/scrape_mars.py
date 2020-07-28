# Import variables and set environment
from splinter import Browser
from bs4 import BeautifulSoup
from twitter_scraper import get_tweets
from twitterscraper import query_tweets
import datetime as dt
import pandas as pd
import requests
import time 

#NASA Mars News
#Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

# Set executable path and variable values to explore
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

# Defining scrape function and create dictionary to hold values
def scrape():
    scraped_data = {}
    scraped_data["latest_news_title"] = mars_news_scrape()
    scraped_data["latest_news_paragraph"] = mars_news_scrape()
    scraped_data["featured_image"] = featured_image()
    scraped_data["mars_weather_twitter"] = mars_weather_twitter()
    scraped_data["mars_facts"] = mars_facts()
    scraped_data["mars_hemisp"] = mars_hemisp()
    return scraped_data


def mars_news_scrape():
    # Scrape the Latest News Title
    # Use Parent Element to Find First <a> Tag and Save it as latest_news_title
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_mars = soup.select_one("ul.item_list li.slide")
    news_mars.find("div", class_="content_title")
    latest_news_title = news_mars.find("div", class_="content_title").get_text()
    # Scrape the Latest Paragraph Text
    latest_news_paragraph = news_mars.find("div", class_="article_teaser_body").get_text()
    return latest_news_title
    return latest_news_paragraph


def featured_image():
    #JPL Mars Space Images - Featured Image
    # Set value of URL explore according to info provided and define variables
    featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(featured_image_url)
    html_img = browser.html
    soup = BeautifulSoup(html_img, "html.parser")
    featured_image_url = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
    main_url = 'https://www.jpl.nasa.gov'
    featured_image_url = main_url + featured_image_url
    return featured_image_url


def mars_weather_twitter():
    # Mars Weather
    # Define variables
    twitter_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(twitter_url)
    # Visit the Mars Weather Twitter Account
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    # Parse Results HTML with BeautifulSoup
    html = browser.html
    weather_soup = BeautifulSoup(html, "html.parser")
    # Scrap Tweets from MarsWxReport
    mars_tweets = []
    for tweet in get_tweets('MarsWxReport', pages=1):
        mars_tweets.append(tweet) # Add values to the list
    # Extract the weather value of the latest MarsWxReport Tweet
    mars_weather_dict = {}
    mars_weather_dict = mars_tweets[0]
    mars_weather = mars_weather_dict.get('text')
    return mars_weather


def mars_facts():
    # Mars Facts
    # Set value of URL explore according to info provided and define variables
    mars_facts_url = 'https://space-facts.com/mars/'
    browser.visit(mars_facts_url)
    # Prepare Pandas dataframe
    mars_facts = pd.read_html(mars_facts_url)
    mars_facts_df = pd.DataFrame(mars_facts[0])
    mars_facts_df.columns = ['Attribute', 'Value']
    # Prepare HTML Table
    mars_fact_table = mars_facts_df.to_html(index = False)
    mars_fact_table = mars_fact_table.replace('\n', '')
    return mars_fact_table

def mars_hemisp():
    # ## Mars Hemispheres
    # Set URL to visit based on reference provided and prepare scraping
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    # define variables and list for scraping
    mars_hemispheres = []
    products = soup.find("div", class_ = "result-list" )
    items = products.find_all("div", class_="item")
    # Iterate to get items (products) from mars hemispheres
    for item in items:
        title = item.find("h3").text
        item_link = item.find("a")["href"]
        image_link = "https://astrogeology.usgs.gov/" + item_link    
        browser.visit(image_link)
        html = browser.html
        soup=BeautifulSoup(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        mars_hemispheres.append({"title": title, "img_url": image_url})
    return mars_hemispheres

# ### End of notebook