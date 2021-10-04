#!/usr/bin/env python
# coding: utf-8

# In[39]:


#Import Splinter and BeautifulSoup 
from splinter import Browser 
from bs4 import BeautifulSoup as soup 
from webdriver_manager.chrome import ChromeDriverManager 
import pandas as pd


# In[40]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless = False)


# In[41]:


# Visit the mars nasa news site

url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page

browser.is_element_present_by_css('div.list_text', wait_time = 1)


# In[42]:


html = browser.html 
news_soup = soup(html, 'html.parser')
slide_elm = news_soup.select_one('div.list_text')


# In[43]:


slide_elm.find('div', class_ = 'content_title')


# In[44]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elm.find('div', class_ = 'content_title').get_text()
news_title


# In[45]:


# Use the parent element to find the paragraph text
news_p = slide_elm.find('div', class_ = 'article_teaser_body').get_text()
news_p


# ## Featured Image 
# 

# In[46]:


# Visit URL
url = 'https://spaceimages-mars.com/'
browser.visit(url)


# In[47]:


# Find and click the full image button

full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[48]:


# Parse the resulting html with soup
html = browser.html 
img_soup = soup(html, 'html.parser')


# In[49]:


# Find the relative image URL 

img_url_rel = img_soup.find('img', class_ = 'fancybox-image').get('src')
img_url_rel


# In[50]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[51]:


df = pd.read_html('https://galaxyfacts-mars.com/')[0]
df.columns = ['description', 'Mars', 'Earth']
df.set_index('description', inplace = True)
df


# In[52]:


df.to_html()


# In[53]:


browser.quit()


# In[54]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[55]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[56]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[57]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[58]:


slide_elem.find('div', class_='content_title')


# In[59]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[60]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[61]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[62]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[63]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[64]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[65]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[66]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[67]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[68]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[69]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

browser.visit(url)


# In[70]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

# Loop through four of the titles
for item in range(0,4):
    search_link = browser.find_by_css('a.itemLink h3')[item].click()

    open_image = browser.find_by_id('wide-image-toggle').click()

    html = browser.html
    hem_soup = soup(html,'html.parser')

    full_img = hem_soup.find('a',text='Sample').get('href')
    img_title = hem_soup.find('h2',class_='title').get_text()

    # Append information urls into a list of dictionaries with image title as key and link as value
    hemisphere_image_urls.append({'title':img_title, 'img_url': full_img_src})

    browser.back()


# In[72]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[73]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]:




