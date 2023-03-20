from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests


def scrape_info():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    ### NASA Mars News -----------------------
    
    # url for the mars facts page
    url_red_plante = 'https://redplanetscience.com'
    
    # Use the browser to navigate to the given URL.
    browser.visit(url_red_plante)
    
    # create a BeautifulSoup object for the NASA News page
    html = browser.html
    soup = bs(html, 'html.parser')
    
    # the first article of the page
    article = soup.find('div', class_='list_text')
    # the title of the article
    article_title = article.find('div', class_='content_title').text
    # the article text (paragraph)
    article_paragraph = article.find('div', class_='article_teaser_body').text
    
    
    ### JPL Mars Space Images - Featured Image -----------------------
    
    # navigate to the main page
    url_images = 'https://spaceimages-mars.com/'
    browser.visit(url_images)
    
    # find all the image button and clicking on it
    browser.find_by_text(' FULL IMAGE').first.click()

    # getting the image
    img = browser.find_by_css('img.fancybox-image')

    # find the image url
    featured_image_url = img['src']
    
    ### Mars Facts -----------------------
    
    # url for the mars facts page
    url_mars_facts = 'https://galaxyfacts-mars.com'
    # reading the html 
    mars_facts = pd.read_html(url_mars_facts)   
    
    # getting the first item from the list mars_facts
    mars_facts_df = pd.DataFrame(mars_facts[0])

    # assigning the first row of the df as column labels for the DataFrame.
    mars_facts_df.columns = mars_facts_df.loc[0]

    # setting the index 
    mars_facts_df.set_index('Mars - Earth Comparison', inplace=True)

    # dropping not needed column
    mars_facts_df.drop('Mars - Earth Comparison', inplace=True)
    
    mars_facts_table = mars_facts_df.to_html(classes="table table-striped")
    
    ### Mars Hemispheres -----------------------
    
    # navigate to the main page
    url_hemisphere = 'https://marshemispheres.com/'
    browser.visit(url_hemisphere)
    
    # create a BeautifulSoup object for the hemisphere page
    html = browser.html
    soup = bs(html, 'html.parser')
    
    # find all the hemisphere items
    items = soup.find_all('div', class_='item')
    
    # an empty list to store the information
    hemisphere_image_urls = []

    # loop through each item
    for item in items:
        # get the link to the hemisphere page
        link = item.find('a')['href']
        
        # visit the hemisphere page
        browser.visit(url_hemisphere + link)
        
        # create a BeautifulSoup object for the hemisphere page
        html = browser.html
        soup = bs(html, 'html.parser')
        
        # get the title of the hemisphere
        title = soup.find('h2', class_='title').text.strip()
        
        # find the url for the full resolution image
        img_url = soup.find('img', class_='wide-image')['src']
        img_url = url_hemisphere + img_url
        
        # create a dictionary for the hemisphere information and append it to the list
        hemisphere_info = {'title': title, 'img_url': img_url}
        hemisphere_image_urls.append(hemisphere_info)
        
        # go back to the main page
        browser.back()  
    
    
    # Small images 
    # an empty list to store the information
    sm_hemisphere_title_url = []
    
    # loop through each item
    for item in items:
        
        sm_img_title = item.find('h3').text
        sm_img = item.find('img', class_='thumb')['src']
        sm_hemisphere_title_url.append({'title':sm_img_title, 'img_url':sm_img})
    
        
    mars_info_dict = {
        'title': article_title,
        'paragraph': article_paragraph,
        'featured_img': featured_image_url,
        'mars_facts': str(mars_facts_table),
        'hemisphere_img': hemisphere_image_urls,
        'sm_hemisphere_img': sm_hemisphere_title_url
    }
    
    print(mars_info_dict)
    
    browser.quit()
    
    return mars_info_dict