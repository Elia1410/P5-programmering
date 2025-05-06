import json
from random import randint, random, choice, choices

class Game:
    def __init__(self):
        self.__level = 0
        self.__previousQuestions = [[], [], []]
        
        with open("output2.json", "r", encoding="utf8") as file:
            self.__questionData = json.load(file)

        self.__currentQuestion = self.__newQuestion()

    def getLevel(self):
        return self.__level
    
    def nextLevel(self):
        if self.__level < 14:
            self.__level += 1
        self.__currentQuestion = self.__newQuestion()
    
    def __newQuestion(self):
        qLevel = int(self.getLevel()/5)
        while True:
            qIndex = randint(0, len(self.__questionData[str(qLevel+1)])-1)
            if not qIndex in self.__previousQuestions[qLevel]:
                self.__previousQuestions[qLevel].append(qIndex)
                break
        return self.__questionData[str(qLevel+1)][qIndex]
    
    def getQuestion(self):
        return {
            "question": self.__currentQuestion["question"].replace("&amp;", "&"),
            "options": [option.replace("&amp;", "&") for option in self.__currentQuestion["options"]],
            "answer": self.__currentQuestion["answer"]
        }
    
    def gameOver(self):
        self.__level = 0
        self.__currentQuestion = self.__newQuestion()

    def LLaskAudience(self):
        correctIndex = self.getQuestion()["answer"]
        currLevel = self.getLevel()
        correctAnswerProb = (15-currLevel)*2
        remainingProb = 100-correctAnswerProb

        probabilities = [0, 0, 0, 0]
        probabilities[correctIndex] += correctAnswerProb

        for i in range(remainingProb):
            probabilities[randint(0,3)] += 1
        
        return probabilities

    def LLaskHost(self):
        question = self.getQuestion()
        answer = question["options"][question["answer"]]
        incorrect = list(question["options"])
        incorrect.pop(question["answer"])

        hostKnowledge = random()

        if hostKnowledge > 0.58+0.02*self.getLevel():
            return f"I'm most certain the correct answer is '{answer}'."
        elif hostKnowledge > 0.25:
            if random() > 0.5: return f"I'm pretty sure the correct answer is '{answer}'."
            else: f"I'm pretty sure the correct answer is '{choice(incorrect)}'."
        else:
            return "I wouldn't hazard a guess as i am completely out of my depth with this one. Sorry."
            

    def LL5050(self):
        question = self.getQuestion()
        incorrect = [0, 1, 2, 3]
        incorrect.pop(question["answer"])
        incorrect.pop(randint(0,2))
        for i in incorrect:
            self.__currentQuestion["options"][i] = ""
        return incorrect
    

    def LLcallFriend(self):
        question = self.getQuestion()
        answer = question["options"][question["answer"]]
        incorrect = list(question["options"])
        incorrect.pop(question["answer"])

        hostKnowledge = random()

        if hostKnowledge > 0.45+0.02*self.getLevel():
            return f"It's absolutely '{answer}'. I'm certain."
        elif hostKnowledge > 0.20:
            if random() > 0.5: return f"I think it's '{answer}' but i can't be sure"
            else: f"I think it's '{choice(incorrect)}' but i can't be sure."
        else:
            return "I'm sorry, i just have no idea. Good luck."

if __name__ == "__main__":
    game = Game()
    while True:
        question = game.getQuestion()["question"]
        options = game.getQuestion()["options"]
        level = game.getLevel()

        print(f"level {level+1}: {question}\n")
        print(f"(1) {options[0]}")
        print(f"(2) {options[1]}")
        print(f"(3) {options[2]}")
        print(f"(4) {options[3]}\n")
        print(f"L1: ask the audience  L2: ask the host  L3: 50:50  L4: call a friend")
        
        while True:
            guess = input("(1-4 or L1-L4): ")
            if guess.isdigit():
                if int(guess) in range(1,5):
                    break
            else:
                if guess.upper() == "L1":
                    print(game.LLaskAudience())
                elif guess.upper() == "L2":
                    print(game.LLaskHost())
                elif guess.upper() == "L3":
                    print(game.LL5050())
                elif guess.upper() == "L4":
                    print(game.LLcallFriend())

        if game.getQuestion()["answer"] == int(guess)-1:
            print("CORRECT!!!\n")
            game.nextLevel()
        else:
            print("INCORRECT!!!\n")
            game.gameOver()
