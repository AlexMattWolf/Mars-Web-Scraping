# Mars-Web-Scraping

## Project Objectives
This goal of this project was to understand the principles behind a web-scraping and social media mining via building a script. This script would have to use 5 different websites, and through the use Beautiful Soup and Splinter, navigate the sites to find particular pieces of text, image URLs, and tables.

#### Project Status: Complete

### Methods
* Web Scraping
* Social Media Mining
* Flask Deployment
* MongoDB

### Technologies
* NoSQL
* GitBash
* Python 
    * Jupyter Notebook/Lab
    * Pandas
    * Beautiful Soup
    * Splinter
    * Pandas
    * Time
    * Flask
    * Flask_Pymongo
* HTML
    * Bootstrap
    * CSS

## Project Description

In the initial stages of the project, the scraper was built in Jupyter Lab as there the process could be built in individual stages with visible results. The results would then be stored in a dictionary format. The project scraped 5 websites list in the following table, as well as, which pieces of the sites were scraped.

|Site     |Variables Extracted  |
|---------|--------------------|
| [Mars NASA](https://mars.nasa.gov/news/) | The most recent news story's title & abstract about Mars. |
| [JPL NASA](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) | The URL to the current featured, high-resolution image about Mars. |
| [Mars Weather Twitter](https://twitter.com/marswxreport?lang=en) | Mars' weather in the most recent post. |
| [Space Facts](https://space-facts.com/mars) | Table about Mars' facts |
| [Astrogeology USGS](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) | High resolution pictures of each hemisphere and their names |

Once this step was complete and pieces were successfully collected, the Jupyter Lab file, *mission_to_mars.ipynb* , was converted to a python file, *scrape_mars.py*. This was achieved by GitBash via the following code: 

* jupyter nbconvert --to script mission_to_mars.ipynb

After conversion, using Flask, the dictionary of results was uploaded into MongoDB, creating a NoSQL database. Through flask, this database would be used to import the dictionary of results directly into the HTML file. This would allow users to simply click a button to execute *scrape_mars.py*, and receieve the most recent pieces that have been uploaded and updated in the sourced websites, all without leaving the HTML website.


## Launching the App Locally
**Note**: Must have GitBash and MonogDB installed and Chrome Driver Path.

1. Clone This Repo to A Local File

2. Using GitBash, launch the app.py: 
* python app.py

2.5. If initially running this app, in a different instance of GitBash use the following code.
* mongod

3. Next, in your preferred web browser type _127.0.0.1:5000_ into the URL. 
4. Press the "Initiate Space Exploration Button" and let Chrome Driver run without interruption. Do not close.

## Potential Issues
* As the sites are updated, differing formats would have to be corrected for as the HTML could to locate those variables could have been changed. This would result in an error when trying to run the web scraper.

## Author

| Alex Wolf | https://github.com/AlexMattWolf |

