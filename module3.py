from selenium import webdriver
import csv
from bs4 import BeautifulSoup
import module2
from module2 import getDetails
import re
import time
import pandas as pd

f= open('html.txt','r',encoding='utf16')
htmlSource = f
f.close
soup = BeautifulSoup(htmlSource)
soup.prettify()

organization =[]
category=[]
opportunity_number = []
location=[]
for link in soup.find_all('p','opportunity-title-text'):
    for a in link.childGenerator():
        #print(str(a))
        category.append(str(a))



              
for link in soup.find_all('p','custom-label'):
    if(link.text == 'Location'):
        for a in link.childGenerator():
            print(str(a))
    
detailsList=[]
i=0
for link in soup.find_all('div','opportunity-title-box text-center'):
    i=i+1
    opportunity_number.append(link.next.attrs['href'])
    detailsList.append(getDetails('http://aiesec.org' + link.next.attrs['href']))

my_df2=pd.DataFrame(detailsList)
my_df2.to_csv('my_csv20.csv')
