# web-scraping-challenge

## Part 1
For this challange we completed the scraping by using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter. 

Firts, we created a Jupyter Notebook file called `mission_to_mars.ipynb` and used this to complete all of your scraping and analysis tasks. W srape the [Mars News Site](https://redplanetscience.com/) and collected the latest News Title and Paragraph Text. We assigned the text to variables.

Then, we visited the Featured Space Image site [here](https://spaceimages-mars.com).
We used splinter to navigate the site and find the image url for the current Featured Mars Image and assigned the url string to a variable called `featured_image_url`.

After that, we visited the Mars Facts webpage [here](https://galaxyfacts-mars.com) and we used Pandas to scrape the table which contains the facts about the planet including Diameter, Mass, etc. We used Pandas to convert the data to a HTML table string.

At last, we visited the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres. We "clicked" on each of the links to the hemispheres in order to find the image url to the full resolution image. We saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. We used Python dictionary to store the data using the keys `img_url` and `title`. Then we append the dictionary with the image url string and the hemisphere title to a list.

## Part 2

We used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

We started by converting our Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
Next, we created a route called `/scrape` that will import the `scrape_mars.py` script and call the `scrape` function. We stored the return value in Mongo as a Python dictionary.
We created a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data. Then, we added a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. We also added a functional button "Scrape New Data" to the main page.
