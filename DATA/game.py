import json
from random import randint, random, choice

import sys
import os

# hent den aktuelle sti
try:
    PATH = sys._MEIPASS  # PyInstaller 
except AttributeError:
    PATH = os.path.abspath(".")

class Game:
    """Klasse til spillogik"""
    def __init__(self):
        """Initialiser Game-objekt"""
        
        self.__level = 0 # niveau af pengesum
        self.__previousQuestions = [[], [], []] # lister af allerde-brugte spørgsmål
        
        # importer alle spørgsmål fra JSON fil 
        with open(os.path.join(PATH,"DATA/output2.json"), "r", encoding="utf8") as file:
            self.__questionData = json.load(file)

        self.__currentQuestion = self.__newQuestion()

    def getLevel(self):
        """ Få det nuværende niveau

        Returns:
            int: niveau af nuværende pengesum i spillet
        """
        return self.__level
    
    def nextLevel(self):
        """ Sætter spillet til næste spørgsmål og inkrementer niveau"""
        if self.__level < 14:
            self.__level += 1
        self.__currentQuestion = self.__newQuestion()
    
    def __newQuestion(self):
        """Hent et nyt spørgsmål fra questionData.

        Returns:
            Dict: Et spørgsmål i følgende format:

                Question = {
                    "question": str,
                    "options": [str, str, str, str],
                    "answer": int
                }
        """

        qLevel = int(self.getLevel()/5) # omdan niveau (0-14) til spørgsmålsniveau (1-3)

        # repeter indtil et nyt spørgsmål findes som ikke er i self.__previousQuestions
        while True:
            qIndex = randint(0, len(self.__questionData[str(qLevel+1)])-1) # random spørgsmålindeks
            if not qIndex in self.__previousQuestions[qLevel]:
                self.__previousQuestions[qLevel].append(qIndex) # gem spørgsmål til allerede-brugte spørgsmål
                break
        return self.__questionData[str(qLevel+1)][qIndex]
    
    def getQuestion(self):
        """Hent et nyt spørgsmål fra questionData og formater korrekt.

        Returns:
            Dict: Et spørgsmål i følgende format:

                Question = {
                    "question": str,
                    "options": [str, str, str, str],
                    "answer": int
                }
        """
        return {
            "question": self.__currentQuestion["question"].replace("&amp;", "&"),
            "options": [option.replace("&amp;", "&") for option in self.__currentQuestion["options"]],
            "answer": self.__currentQuestion["answer"]
        }
    
    def gameOver(self):
        """reset niveau og få nyt spørgsmål"""
        self.__level = 0
        self.__currentQuestion = self.__newQuestion()

    def LLaskAudience(self):
        """Life line: Spørg publikum

        Simmulerer publikumsvar, hvor jo højere niveau er, 

        jo mindre sikkerhed er der i det korrekte svar

        Returns:
            List: liste af "publikums" valg i procenter 0-100% (int)
        """
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
        """ Life line: Spørg værten

        Simulerer chancen for at værten "kender" svaret:

        P1 = 42% - (2% * level): chancen for at værten med 100% sikkerhed kan svaret
        
        P2 = 75% - P1: chancen for at værten måske kan svaret (50% sikker)

        P3 = 100% - P2: chancen for at værten ikke kan svaret

        Returns:
            Str: Værtens svar
        """
        question = self.getQuestion()
        answer = question["options"][question["answer"]]
        incorrect = list(question["options"])
        incorrect.pop(question["answer"])

        hostKnowledge = random() # tilfældigt tal der betemmer hvor meget værten "ved"

        if hostKnowledge > 0.58+0.02*self.getLevel(): # > 58% + ( 2% * niveau ) 
            return f"I'm most certain the correct answer is '{answer}'."
        elif hostKnowledge > 0.25: # > 25%
            if random() > 0.5: return f"I'm pretty sure the correct answer is '{answer}'."
            else: return f"I'm pretty sure the correct answer is '{choice(incorrect)}'."
        else:
            return "I wouldn't hazard a guess as i am completely out of my depth with this one. Sorry."
            

    def LL5050(self):
        """ Life line: 50:50

        Udelukker 2 af de forkerte svarmuligheder

        Returns:
            List: indeks af svar der udelukkes 
        """
        question = self.getQuestion()
        incorrect = [0, 1, 2, 3]
        incorrect.pop(question["answer"])
        incorrect.pop(randint(0,2))
        for i in incorrect:
            self.__currentQuestion["options"][i] = ""
        return incorrect
    

    def LLcallFriend(self):
        """ Life line: Ring til en ven

        Simulerer chancen for at vennen "kender" svaret:

        P1 = 55% - (2% * level): chancen for at vennen med 100% sikkerhed kan svaret
        
        P2 = 80% - P1: chancen for at vennen måske kan svaret (50% sikker)

        P3 = 100% - P2: chancen for at vennen ikke kan svaret

        Returns:
            Str: Vennens svar
        """

        question = self.getQuestion()
        answer = question["options"][question["answer"]]
        incorrect = list(question["options"])
        incorrect.pop(question["answer"])

        friendKnowledge = random() # tilfældigt tal der betemmer hvor meget vennen "ved"

        if friendKnowledge > 0.45+0.02*self.getLevel():
            return f"It's absolutely '{answer}'. I'm certain."
        elif friendKnowledge > 0.20:
            if random() > 0.5: return f"I think it's '{answer}' but i can't be sure"
            else: return f"I think it's '{choice(incorrect)}' but i can't be sure."
        else:
            return "I'm sorry, i just have no idea. Good luck."

# test af Game-objektets funktionalitet
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
