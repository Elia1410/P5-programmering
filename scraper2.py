from bs4 import BeautifulSoup as bs
import requests
import json
from concurrent.futures import ThreadPoolExecutor

level1Questions = []
level2Questions = []
level3Questions = []

def addQuestion(question: str, options: list, answer: str, outputDict):
        outputDict.append({
            "question": question,
            "options": options,
            "answer": options.index(answer[3:])
        })

def scrapeURL(url):
    page = requests.get(url)

    scraper = bs(page.text, "html.parser")

    scraperText = scraper.prettify().split("\n")
    scraperTextStripped = [line.strip() for line in scraperText]


    for i, line in enumerate(scraperTextStripped):
        try:
            if line[0] == "$":

                question = scraperTextStripped[i+2]

                optionsRaw = scraperTextStripped[i+4] + scraperTextStripped[i+6]
                
                a = ""
                b = ""
                c = ""
                d = ""

                cursor = 3
                
                while optionsRaw[cursor+3] != ":":
                    a += optionsRaw[cursor]
                    cursor += 1
                cursor += 5
                
                while optionsRaw[cursor+1] != ":":
                    b += optionsRaw[cursor]
                    cursor += 1
                cursor += 3
                
                while optionsRaw[cursor+3] != ":":
                    c += optionsRaw[cursor]
                    cursor += 1
                cursor += 5

                d = optionsRaw[cursor:]

                nextLine =  i+8
                while '<div class="spoiler-body">' not in scraperTextStripped[nextLine]:
                    nextLine += 1
                
                answer = scraperTextStripped[nextLine+1]

                money = int(line[1:].replace(",", ""))
                if money <= 1000:
                    addQuestion(question, [a, b, c, d], answer, level1Questions)
                elif money < 50000:
                    addQuestion(question, [a, b, c, d], answer, level2Questions)
                else:
                    addQuestion(question, [a, b, c, d], answer, level3Questions)

                print(f"added 1 question from {url[-5:]}")     
        except:
            print(f"failed 1 question from {url[-5:]}")


URLsToScrape = 700

URLs = []


for i in range(URLsToScrape):
    try:
        mainPage = requests.get(f'https://www.wwtbambored.com/viewforum.php?f=3&start={i+1}')
        scraper = bs(mainPage.text, "html.parser")
        scraperText = scraper.prettify().split("\n")
        scraperTextStripped = [line.strip() for line in scraperText]

        transcriptPageURL = "https://www.wwtbambored.com/viewtopic.php?f=1&t="

        for n, line in enumerate(scraperTextStripped):
            if 'row bg2' in line:
                URLLine = scraperTextStripped[n+4]
                tIndex = URLLine.index("t=")
                transcriptPageURL += URLLine[tIndex+2:tIndex+7]
                break

        URLs.append(transcriptPageURL)
        print(f"{i+1}/{URLsToScrape} url gathered")
    except:
        print("URL failed")

with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(scrapeURL, URLs)


output = {
    "1": level1Questions,
    "2": level2Questions,
    "3": level3Questions
}

with open("output2.json", "w", encoding='utf-8') as file:
    json.dump(output, file, indent=4, ensure_ascii=False)