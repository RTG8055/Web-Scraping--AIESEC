# Web-Scraping--AIESEC
dynamic web scraping the Aiesec website

module1 contains the script to load the opportunities page to be scraped, scroll till the end so that all the offers are loaded (sleep time can be changed depending on the net speed) and save the source in a text file.
module2 contains the script for scraping individual offers( is used by the module 3 file)
module3 contains used the html page stored in module1 as input to fetch all the urls for each offer and get the details and save it in csv format- offer wise
