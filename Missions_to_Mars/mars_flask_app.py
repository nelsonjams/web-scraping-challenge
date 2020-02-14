
#variable name1, variable name2 = scrape_py.whatever you def name1

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")

#route to render index.html template using data from Mongo
@app.route("/")
def index():
    mars_dict = mongo.db.mars_dict.find_one()
    return render_template("index.html", mars=mars_dict)


@app.route("/scrape")
def scrape():
    mars_dict = mongo.db.mars_dict
    mars_data = scrape_mars.scrape()
    #update the mongo database using update and upsert
    mars_dict.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
