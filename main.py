from bs4 import BeautifulSoup as bs
import requests

URL = 'https://www.wwtbambored.com/viewtopic.php?f=1&t=62961'
page = requests.get(URL)

scraper = bs(page.text, "html.parser")

scraperText = scraper.prettify().split("\n")
scraperTextStripped = [line.strip() for line in scraperText]   

for i, line in enumerate(scraperTextStripped):
    if line[0] == "$":
        print(scraperTextStripped[i+2])
        print(scraperTextStripped[i+4])
        print(scraperTextStripped[i+6])
        nextLine =  i+8
        while '<div class="spoiler-body">' not in scraperTextStripped[nextLine]:
            nextLine += 1
        print(scraperTextStripped[nextLine+1])
        print("\n\n")