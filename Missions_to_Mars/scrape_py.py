from splinter import Browser
import requests
from selenium import webdriver
#BEAUTFILSOUP ALLOWS US TO VISIT WEBPAGES 
from bs4 import BeautifulSoup
import pandas as pd
import pprint
import pymongo
# open chrome driver
def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
#Scrape NASA Mars News Site for the Latest Article and its Text
def mars_news():
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    # HTML object
    html=browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Collect the latest News Title 
    news_title = soup.find("div", class_="content_title").text
    print(news_title)
    #and Paragraph Text
    news_p = soup.find("div", class_ ="article_teaser_body").text
    print(news_p)
#Scrape JPL for Featured Space Image and Save Large Image using splinter
def jpl_image():
#image location
    img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(img_url)

    # HTML object
    html=browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    #use soup to locate image
    img_url = soup.find('article', class_='carousel_item')['style']
    print(img_url)
    #extract url appendage from style text
    split_text = img_url.split("'")
    print(split_text[1]) 
    #add url appendage to main jpl url 
    featured_image_url = f'https://www.jpl.nasa.gov{split_text[1]}'
    print(featured_image_url)   
#Scrape Latest Mars Weather Tweet from its Twitter Account
def mars_weather():
    tweet_url = 'https://twitter.com/marswxreport?lang=en'
    # Retrieve page with the requests module
    response_weather = requests.get(tweet_url)
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(response_weather.text, 'lxml')
    mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text.strip()
    print(mars_weather)
 #Scrape Mars Facts Webpage for Planet Facts
 def mars_facts():
    import pandas as pd
    mars_facts_url = 'https://space-facts.com/mars/'
    browser.visit(mars_facts_url)
    # HTML object
    html=browser.html
    #read html into pandas
    facts_table = pd.read_html(mars_facts_url)
    facts_table[0]
    #check the columns
    mars_facts_df = facts_table[0]
    mars_facts_df.columns = mars_facts_df.columns.astype(str)
    mars_facts_df.columns
    #set the index
    mars_facts_df.set_index('0')
    mars_facts_df
    #rename columns
    mars_facts_df.rename({"0":"Descriptor", "1":"Value"},axis=1,inplace=True)
    # mars_facts_df.columns = ['Descriptor','Value']
    mars_facts_df
    #convert dataframe into html table
    html_table = mars_facts_df.to_html()
    html_table
    #save facts to html
    mars_facts_df.to_html('facts_table.html')
# Obtain 4 Mars Hemispheres Images
def mars_hemispheres():
    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemispheres_url)
    html=browser.html
    soup=BeautifulSoup(html, 'html.parser')
    #click on the link to Cerberus hemisphere
    cerberus_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(cerberus_url)
    html=browser.html
    soup=BeautifulSoup(html, 'html.parser')
    #use beautiful soup to grab image
    cerberus = soup.find('div', class_ = 'downloads')
    cerberus_link = cerberus.find('a')
    cerberus_href = cerberus_link['href']

    print(cerberus_href)
    #click on the link to Schiaparelli hemisphere
    schiaparelli_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(schiaparelli_url)
    html=browser.html
    soup=BeautifulSoup(html, 'html.parser')
    #use beautiful soup to grab image
    schiaparelli = soup.find('div', class_ = 'downloads')
    schiaparelli_link = schiaparelli.find('a')
    schiaparelli_href = schiaparelli_link['href']
    print(schiaparelli_href)
    #click on the link to Syrtis Major hemisphere
    Syrtis_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    browser.visit(Syrtis_url)
    html=browser.html
    soup=BeautifulSoup(html, 'html.parser')
    #use beautiful soup to grab image
    Syrtis = soup.find('div', class_ = 'downloads')
    Syrtis_link = Syrtis.find('a')
    Syrtis_href = Syrtis_link['href']
    print(Syrtis_href)
    #click on the link to Valles Marineris hemisphere
    valles_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    browser.visit(valles_url)
    html=browser.html
    soup=BeautifulSoup(html, 'html.parser')
    #use beautiful soup to grab image
    valles = soup.find('div', class_ = 'downloads')
    valles_link = valles.find('a')
    valles_href = valles_link['href']

    print(valles_href)

    #save image url and title containing the hemisphere name
    #make library

    hemisphere_image_urls = [
    {'title': "Valles Marineris Hemisphere", 'img_url': valles_href},
    {'title': "Syrtis Major Hemisphere", 'img_url': Syrtis_href},
    {'title': "Schiaparelli Hemisphere", 'img_url': schiaparelli_href},
    {'title': "Cerberus Hemisphere", 'img_url': cerberus_href}
    
    ]
    return hemisphere_image_urls  
