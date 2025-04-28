from bs4 import BeautifulSoup as bs
import requests


page = requests.get('https://www.wwtbambored.com/viewforum.php?f=3')

scraper = bs(page.text, "html.parser")

scraperText = scraper.prettify().split("\n")
scraperTextStripped = [line.strip() for line in scraperText]

