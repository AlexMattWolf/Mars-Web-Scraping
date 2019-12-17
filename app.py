from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    to_mars = mongo.db.to_mars.find_one()
    return render_template("index.html", to_mars=to_mars)

@app.route("/scrape")
def scraper():
    to_mars = mongo.db.to_mars
    to_mars_data = scrape_mars.scrape()

    to_mars.update({}, to_mars_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)