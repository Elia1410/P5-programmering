from bs4 import BeautifulSoup as bs
import requests
import json
from concurrent.futures import ThreadPoolExecutor

# niveauer til forskellige pengemængder
level1Questions = [] # x < 1000$
level2Questions = [] # 1000$ < x < 50000$
level3Questions = [] # x > 50000$

def addQuestion(question: str, options: list, answer: str, outputDict: list):
        outputDict.append({
            "question": question,
            "options": options,
            "answer": options.index(answer[3:])
        })

def scrapeURL(url):
    """ Tager en URL-adresse som argument, og scraper siden for spørgsmål"""
    page = requests.get(url)

    scraper = bs(page.text, "html.parser") # opret bs4 scraper

    scraperText = scraper.prettify().split("\n") # udvind ren tekst fra scraper
    scraperTextStripped = [line.strip() for line in scraperText] # fjern ekstra mellemrum fra sidetekst

    # iterer over linjer på siden
    for i, line in enumerate(scraperTextStripped):
        try:
            # gå frem indtil $-tegn findes på siden
            if line[0] == "$":
                # tag spørgsmål
                question = scraperTextStripped[i+2]

                # tag linjerne med valgmuligheder
                optionsRaw = scraperTextStripped[i+4] + scraperTextStripped[i+6]
                
                a = ""
                b = ""
                c = ""
                d = ""

                cursor = 3
                
                # formater linjerne med valgmuligheder
                while optionsRaw[cursor+3] != ":": # A
                    a += optionsRaw[cursor]
                    cursor += 1
                cursor += 5
                
                while optionsRaw[cursor+1] != ":": # B
                    b += optionsRaw[cursor]
                    cursor += 1
                cursor += 3
                
                while optionsRaw[cursor+3] != ":": # C
                    c += optionsRaw[cursor]
                    cursor += 1
                cursor += 5

                d = optionsRaw[cursor:] # D

                # gå frem i linjer indtil korrekt svar
                nextLine =  i+8
                while '<div class="spoiler-body">' not in scraperTextStripped[nextLine]:
                    nextLine += 1
                
                answer = scraperTextStripped[nextLine+1] # tag det korrekte svar

                # tilføj data til det korrekte niveau, baseret på pengesummen
                money = int(line[1:].replace(",", ""))
                if money <= 1000:
                    addQuestion(question, [a, b, c, d], answer, level1Questions)
                elif money < 50000:
                    addQuestion(question, [a, b, c, d], answer, level2Questions)
                else:
                    addQuestion(question, [a, b, c, d], answer, level3Questions)                
        except:
            pass


URLsToScrape = 4000 # antal sider der skal skrabes
URLs = []

for i in range(0, URLsToScrape, 50):
    try:
        mainPage = requests.get(f'https://www.wwtbambored.com/viewforum.php?f=3&start={i}') # hent siden med indeks 'i'
        scraper = bs(mainPage.text, "html.parser") # scrape siden
        scraperText = scraper.prettify() # omdan side til tekst

        transcriptPageURL = "https://www.wwtbambored.com/viewtopic.php?f=1&t="

        # hent alle links fra siden
        for i in range(len(scraperText)):
            if scraperText[i] + scraperText[i+1] == "t=":
                transcriptIndex = scraperText[i+2:i+7]
                URLs.append(transcriptPageURL + transcriptIndex)
    except:
        pass

# scrape alle links på forskellige CPU-tråde
# threading anvendes for at spare tid
URLs = list(set(URLs))
with ThreadPoolExecutor(max_workers=75) as executor:
    executor.map(scrapeURL, URLs)

# formater output
output = {
    "1": level1Questions,
    "2": level2Questions,
    "3": level3Questions
}

# print antallet af spørgsmål skrabet for hvert niveau
print("\nQuestions gathered:")
print(f"\ttotal: {len(output['1']) + len(output['2']) + len(output['3'])}")
print(f"\tlevel 1: {len(output['1'])}")
print(f"\tlevel 2: {len(output['2'])}")
print(f"\tlevel 3: {len(output['3'])}")

# gem som JSON
with open("output2.json", "w", encoding='utf-8') as file:
    json.dump(output, file, indent=4, ensure_ascii=False)


"""
Questions gathered:
        total: 2564
        level 1: 873
        level 2: 1593
        level 3: 98
"""

