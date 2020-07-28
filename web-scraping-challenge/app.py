# Import libraries
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

#Flask Setup
#app = Flask(__name__, template_folder='../templates')
app = Flask(__name__)

#Connection Setup
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

#App Setup
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars = mars)

# Scrape Route to Import `scrape_mars.py` Script & Call `scrape` Function
@app.route("/scrape")
def scrappe():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return "Scraping Successful"

# @app.route("/scrape")
# def scrape():
#     mars = mongo.db.mars 
#     mars_data = scrape_mars.scrape()
#     mars.update({}, mars_data, upsert=True)
#     return redirect("http://localhost:5000/", code=302)


# Define Main Behavior
if __name__ == "__main__":
    app.run(debug=True)
