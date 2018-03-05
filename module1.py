from selenium import webdriver
import csv
from bs4 import BeautifulSoup
import re
import time

driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Python36-32\selenium\chromedriver_win32\chromedriver.exe')

url =  'https://aiesec.org/search?type=5'
driver.get(url)
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



htmlSource = driver.page_source
f= open('html.txt','w',encoding='utf16')
f.write(htmlSource)
f.close