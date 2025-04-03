from bs4 import BeautifulSoup as bs
import requests

URL = 'https://www.wwtbambored.com/viewtopic.php?f=1&t=62962'
page = requests.get(URL)

scraper = bs(page.text, "html.parser")

print(scraper.contents)