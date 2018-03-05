from selenium import webdriver
import pandas as pd
import re
from bs4 import BeautifulSoup

def getDetails(url):
    details={}
    details2={}
    driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Python36-32\selenium\chromedriver_win32\chromedriver.exe')
    driver.get(url)
    htmlSource = driver.page_source
    driver.close()

    soup = BeautifulSoup(htmlSource)
    soup.prettify()

    organization=[]
    description=[]
    activities=[]
    prereq=[]
    backgrounds=[]
    skills=[]
    nationalities=[]
    languages=[]
    visaAndLogictics=[]
    selection=[]
    hours=[]
    logistics=[]
    visa=[]
    Insurance=[]
    host=[]
    location=[]

    c=0
    for link in soup.find_all('div','flex-60'):
        if(c>=3):
            continue
        for child in link.children:
            if(c==0):
                try:
                    organization.append(child.text)
                except Exception as e:
                    print(e)
                    try:
                        organization.append(child[:])
                    except Exception as e1:
                        print(e1)
                    else:
                        print('peace')
                else:
                    print('peace')
            elif(c==2):
                location.append(child[:])
            else:
                pass
            c=c+1
        #organization.append(re.sub(r'[\n]+','',link.text))
    for link in soup.find_all('div','content'):
        description.append(re.sub(r'[\n]+','',link.text))

        #0-name and location
        #1-description
        #2-backgrounds
        #3-skills
        #4-nationalities
        #5-languages
        #6-unknown
        #7-selection process
        #13-start date
        #14-end date
        #15-duration
        #16-salary
        #17-positions

    for link in soup.find_all('p','content'):
        activities.append(re.sub(r'[\n]+','',link.text))

    for link in soup.find_all('div','content line pb20 mb20'):
        selection.append(re.sub(r'[\n]+','',link.text))

    for link in soup.find_all('div','prefs'):
        for head in link.find_all('div','pref-heading'):
            if(head.text == 'Backgrounds'):
                #for b in head.children:
                for b in head.find_all('div','small-head'):
                    backgrounds.append(b.text)
                for b in head.find_all('span','content not-match'):
                    backgrounds.append(b.text)
            elif(head.text == 'Skills'):
                for b in head.find_all('div','small-head'):
                    skills.append(b.text)
                for b in head.find_all('span','content not-match'):
                    skills.append(b.text)
            elif(head.text == 'Nationalities'):
                for b in head.find_all('div','small-head'):
                    nationalities.append(b.text)
                for b in head.find_all('span','content not-match'):
                    nationalities.append(b.text)
            elif(head.text == 'Languages'):
                for b in head.find_all('div','small-head'):
                    languages.append(b.text)
                for b in head.find_all('span','content not-match'):
                    languages.append(b.text)
            elif(head.text == 'Working hours'):
                for b in head.find_all('div','small-content'):
                    hours.append(b.text)
                for b in head.find_all('div','italics-content'):
                    hours.append(b.text)
            elif(head.text == 'Logistics'):
                for b in head.find_all('span','text'):
                    logistics.append(b.text)
            elif(head.text == 'Visa'):
                pass
            else:
                break

    try:
        details2['url']=url
        details2['organization']=str(organization[0])
        details2['location']=str(location[0])
        details2['description']=description[1]
        details2['activites']=activities[0]
        details2['selections']=" ".join(description[7].split())
        details2['backgrounds']=" ".join(description[2].split())
        details2['skills']=" ".join(description[3].split())
        details2['natioinalities']=" ".join(description[4].split())
        details2['languages']=" ".join(description[5].split())
        details2['start']=description[13]
        details2['end']=description[14]
        details2['duration']=description[15]
        details2['salary']=description[16]
        details2['positions']=description[17]
    except Exception as e:
        print(e)
    else:
        print(url + ' done')
    return details2