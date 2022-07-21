import requests
from bs4 import BeautifulSoup
import selenium
import chromedriver_autoinstaller
from selenium import webdriver
#Scrape webpage libray
#Text cleaning
import re
import time
#conncet with driver
from selenium.webdriver.common.keys import Keys
chromedriver_autoinstaller.install(cwd=True)
driver = webdriver.Chrome()
driver.get("https://www.dsebd.org/company_listing.php")

links = driver.find_elements("xpath",'//a[@class="ab1 "]')
for link in links:
    print(link.get_attribute("href"))

link_list = [link.get_attribute('href') for link in links]
print(type(link_list))
print(link_list)
#open a new tab to execute link
for i in link_list:
    driver.get(i)
    driver.execute_script("window.open(i,'new window')")





def scroll_to_end_of_page(driver):
    SCROLL_PAUSE_TIME = 2
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

# Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


'''link_lists=[]

for link in links:
    link_lists = 'https://www.dsebd.org/displayCompany.php?name=' + link
    print(link_lists)
    link_lists.append(link_lists)'''

