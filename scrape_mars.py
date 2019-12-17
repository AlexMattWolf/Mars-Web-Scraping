#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import time

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


# In[2]:

def scrape():
    #Set up Urls to sites for scraping
    nasa_url = 'https://mars.nasa.gov/news/'
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    twit_url = 'https://twitter.com/marswxreport?lang=en'
    facts_url = 'https://space-facts.com/mars/'
    usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


    # In[3]:


    #Chrome driver path
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    stop = 5


    # In[4]:


    #Scrape latest news by finding first (latest) headline and tease.
    browser.visit(nasa_url)
    i = 0

    #Code runs faster than brower? Error "Nonetype", use while loops to re-run code if doesn't work first time but only rerun max
    # 3 times. IF still errors may NEED RESTART
    while i < stop:
        try:
            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')
            
            nasa_title = soup.find('div', class_='content_title').text
            nasa_tease = soup.find('div', class_='article_teaser_body').text
            i = stop
        except:
            i += 1
        
        
    # print(nasa_title)
    # print(nasa_tease)


    # In[5]:


    #Scrape latest featured jpl image by navigating to image details pages through full image button > more info button
    browser.visit(jpl_url)
    i = 0

    while i < stop:
        try:
            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')

            #Click full image button so more info button becomes visible
            browser.find_link_by_partial_text('FULL IMAGE').first.click()
            i = stop
        except:
            i += 1
            

    #slow down, page may not be keeping up with code speed. errors out when code executes faster than page loads.
    time.sleep(5)
    i = 0

    while i < stop:
        try:
            #reload html with more info button now visible
            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')
            browser.find_link_by_partial_text('more info').first.click()

            #load new html of new url
            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')

            img = soup.find('img', class_='main_image')
            featured_image_url = 'https://www.jpl.nasa.gov' + img['src']
            i = stop
        except:
            i += 1
            

    # print(featured_image_url)


    # In[6]:


    #Scrape twitter for latest mars weather tweet. If there's a picuture in tweet, exclude picuture reference text.
    browser.visit(twit_url)
    i = 0

    while i < stop:
        try:
            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')

            twit = soup.find('p', class_='TweetTextSize')
            mars_weather = twit.text

            i = stop
        except:
            i += 1

    #filter out picture references/text
    pics = ['…pic', 'pic.twitter']

    for x in pics:
        if x in mars_weather:
            mars_weather = twit.text.split(x)[0]

    # print(mars_weather)


    # In[7]:


    #Get tables from space facts, select only mars facts table, save in html formal and remove newline codes 
    attrs = {'id': 'tablepress-p-mars-no-2'}
    tables = pd.read_html(facts_url, attrs = attrs)

    col = ["Mars", "Facts"]

    Mars_df = tables[0]
    Mars_df.columns = col
    # Mars_df = Mars_df.set_index(col[0]).reset_index()
    Mars_tb = Mars_df.to_html(index = False).replace('\n', '').replace('style="text-align: right;"', '')\
    .replace('border="1"', '')

    # Mars_tb


    # In[8]:


    #Scrape high resolution picutres of Mars' hemispheres, first get list of links on page, then iterate through links returning to 
    # homepage then selecting next link using for loop. 
    browser.visit(usgs_url)
    i = 0

    while i < stop:
        try:
            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')

            link = soup.find_all('h3')
            i = stop
        except:
            i += 1

    link_ls = [x.text for x in link]

    usgs_ls = []

    # print(link_ls)
    j = 0
    i = 0

    for x in link_ls:
        while i < stop:
            try:
                browser.visit(usgs_url)
                browser.click_link_by_partial_text(x)
                
                html = browser.html
                soup = BeautifulSoup(html, 'html.parser')
                i = stop
            except:
                i += 1
        
        img = soup.find('img', class_="wide-image")
        url = ('https://astrogeology.usgs.gov' + img['src'])
        usgs_ls.append({'titles': link_ls[j], "img_url": url})
        j += 1
        
    # usgs_ls

    # In[9]:

    browser.quit()

    #Setup dictionary for all outputs
    to_mars = {'nasa_title': nasa_title, 'nasa_tease': nasa_tease, 'jpl': featured_image_url, 'mars_weather': mars_weather,'facts': Mars_tb, 'usgs': usgs_ls}
    return to_mars


# In[ ]:



