from bs4 import BeautifulSoup as bs
import requests
import json

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
        except:
            pass

links= [
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=62962',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=62934',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=62933',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=62906',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=62889',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=62888',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=62878',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=62876',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=62853',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=62851',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=62811',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=62809',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=62774',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=62773',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=58818',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=58816',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=58235',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=58224',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=58210',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=58206',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=58167',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=58128',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=58118',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=58096',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=58084',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=58074',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=58069',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=58068',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=58043',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=58042',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=58033',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=58027',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=58026',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=58004',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=58003',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57988',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57987',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57981',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57972',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57931',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57917',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57903',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57886',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57876',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57853',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57848',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57819',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57795',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57794',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57773',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57772',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57771',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57764',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57737',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57687',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57627',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57592',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57591',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57564',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57526',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57520',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57519',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57487',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57486',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57390',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57305',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57278',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57160',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57120',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57119',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57096',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57042',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57038',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57026',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=57014',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56975',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56969',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56956',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56940',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56834',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56765',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56679',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56676',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56661',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56644',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56608',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56607',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56575',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56537',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56510',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56535',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56349',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56348',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56321',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56220',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56212',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56188',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56140',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56139',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=56068',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=55537',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=55523',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=55466',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=55458',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=55445',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=55444',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=55414',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=55392',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=55385',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=55295',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=55292',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=55291',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=55274',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=55273',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=55234',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=55211',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=55210',
    'https://www.wwtbambored.com/viewtopic.php?f=1&t=55191'
]


for i, url in enumerate(links):
    scrapeURL(url)
    print(f"scraped: {i+1}")

output = {
    "1": level1Questions,
    "2": level2Questions,
    "3": level3Questions
}

with open("output.json", "w", encoding='utf-8') as file:
    json.dump(output, file, indent=4, ensure_ascii=False)
