import json
from random import randint

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
        return self.__currentQuestion
    
    def gameOver(self):
        self.__level = 0
        self.__currentQuestion = self.__newQuestion()

    def LLaudience(self):
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
        return "bla bla bla"

    def LL5050(self):
        return [1, 2]

    def LLcallFriend(self):
        return "bla bla bla bla"

if __name__ == "__main__":
    game = Game()
    for i in range(15):
        print(f"{game.LLaudience()} on level {game.getLevel()} with answer {game.getQuestion()["answer"]}")
        game.nextLevel()

    """
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
        
        while True:
            guess = input("(1-4): ")
            if guess.isdigit():
                if int(guess) in range(1,5):
                    break

        if game.getQuestion()["answer"] == int(guess)-1:
            print("CORRECT!!!\n")
            game.nextLevel()
        else:
            print("INCORRECT!!!\n")
            game.gameOver()
    """
