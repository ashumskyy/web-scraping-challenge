from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route("/")
def home(): 
    mars_collect = mongo.db.mars_db.find_one()
    
    return render_template("index.html", mars=mars_collect)

@app.route("/scrape")
def scrape():
    # Run the scrape function
    mars_data = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars_db.update_one({}, {"$set": mars_data}, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)