import json

with open("output2.json", "r", encoding="utf8") as file:
    data = json.load(file)

level1Questions = []
level2Questions = []
level3Questions = []

for q in data["1"]:
    seen = False
    for Q in level1Questions:
        if Q["question"] == q["question"]:
            seen = True
            break
    if not seen:
        level1Questions.append(q)
    print(q["question"])

for q in data["2"]:
    seen = False
    for Q in level2Questions:
        if Q["question"] == q["question"]:
            seen = True
            break
    if not seen:
        level2Questions.append(q)
    print(q["question"])

for q in data["3"]:
    seen = False
    for Q in level3Questions:
        if Q["question"] == q["question"]:
            seen = True
            break
    if not seen:
        level3Questions.append(q)
    print(q["question"])


outputNoDupes = {
    "1": level1Questions,
    "2": level2Questions,
    "3": level3Questions
}

with open("output2.json", "w", encoding='utf-8') as file:
    json.dump(outputNoDupes, file, indent=4, ensure_ascii=False)
