from bs4 import BeautifulSoup as bs
import requests
import json

URL = 'https://www.wwtbambored.com/viewtopic.php?f=1&t=62961'
page = requests.get(URL)

scraper = bs(page.text, "html.parser")

scraperText = scraper.prettify().split("\n")
scraperTextStripped = [line.strip() for line in scraperText]

output = []

def addQuestion(question: str, options: list, answer: str):
    output.append({
        "question": question,
        "options": options,
        "answer": options.index(answer[3:])
    })

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

            addQuestion(question, [a, b, c, d], answer)
    except:
        pass

with open("output.json", "w") as file:
    json.dump(output, file, indent=4)




"A: Ghost hunting B: Duck huntingC: Bargain hunting D: Corporate headhunting"