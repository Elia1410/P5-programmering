import pygame as pg
import pygame_widgets
from pygame_widgets.button import Button

from time import sleep

from game import Game

from soundPlayer import Sound

import threading

pg.init()

screen = pg.display.set_mode((900,700))
center = (screen.get_width()/2, screen.get_height()/2)
centerX = screen.get_width()/2 
centerY = screen.get_height()/2
pg.display.set_caption("WWTBAM")
clock = pg.Clock()
FPS = 60

from assets import *
from widget import Button, Toggle
                
def checkWidgets():
    for w in widgets:
        w.checkPressed(screen)

def drawWidgets():
    for w in widgets:
        w.draw(screen)

#buttons
    #anwser buttons 
def selectedA():
    if popUpShown == False:
        selectedStates[0] = True
        sound.playSoundButton()
def selectedB():
    if popUpShown == False:
        selectedStates[1] = True
        sound.playSoundButton()
def selectedC():
    if popUpShown == False:
        selectedStates[2] = True
        sound.playSoundButton()
def selectedD():
    if popUpShown == False:
        selectedStates[3] = True
        sound.playSoundButton()

anwserBtnA = Button(433-93,  632-593, destA[0], destA[1], selectedA, hoverImage=hoverAnwser)
anwserBtnC = Button(433-93,  682-643, destC[0], destC[1], selectedC, hoverImage=hoverAnwser)
anwserBtnB = Button(800-460, 632-593, destB[0], destB[1], selectedB, hoverImage=hoverAnwser)
anwserBtnD = Button(800-460, 682-643, destD[0], destD[1], selectedD, hoverImage=hoverAnwser)

    #lifelines
def usedAskAudience():
    global popUpType, popUpShown, propabilities
    if popUpShown == False and selectedStatesLL[0] == False:
        propabilities = game.LLaskAudience()
        popUpShown = True
        popUpType = "AA"
        selectedStatesLL[0] = True
        sound.playSoundButton()
def usedAskHost():
    global popUpType, popUpShown, hostAnswer
    if popUpShown == False and selectedStatesLL[1] == False:
        hostAnswer = game.LLaskHost()
        popUpShown = True
        popUpType = "AH"
        selectedStatesLL[1] = True
        sound.playSoundButton()
def used5050():
    if popUpShown == False:
        if selectedStatesLL[2] == False:
            game.LL5050()
            selectedStatesLL[2] = True
            sound.playSoundButton()
def usedCallFriend():
    global popUpType, popUpShown, friendAnswer
    if popUpShown == False and selectedStatesLL[3] == False:
        friendAnswer = game.LLcallFriend()
        popUpShown = True
        popUpType = "CF"
        selectedStatesLL[3] = True
        sound.playSoundButton()

LLaskAudienceBtn = Button(85, 52, destAskAudience[0], destAskAudience[1], usedAskAudience, askAudience, hoverLL)
LLaskHostBtn     = Button(85, 52, destAskHost[0],     destAskHost[1],     usedAskHost,     askHost,     hoverLL)
LL5050Btn        = Button(85, 52, dest5050[0],        dest5050[1],        used5050,        fiftyFifty,  hoverLL) 
LLcallFriendBtn  = Button(85, 52, destCallFriend[0],  destCallFriend[1],  usedCallFriend,  callFriend,  hoverLL)

    #popUp
def closePopUp():
    global popUpShown
    popUpShown = False
    sound.playSoundButton()

closePopUpBtn = Button(250, 45, centerX-popUp.get_size()[0]/2+100, 330, closePopUp, closeContinue) 

    #sound
soundTgl = Toggle(83, 74, 30, 30, True, (soundOn, soundOff), (soundOnHover, soundOffHover))

# list of all widgets
widgets = [anwserBtnA, anwserBtnB, anwserBtnC, anwserBtnD, LLaskAudienceBtn, LLaskHostBtn, LL5050Btn, LLcallFriendBtn, soundTgl]


#state variables for buttons
    #anwsers
selectedStates = [False, False, False, False]
correctStates = [False, False, False, False]
    #lifelines
selectedStatesLL = [False, False, False, False]
usedStatesLL = [False, False, False, False]

def drawStates():
    for i, state in enumerate(selectedStates):
        if state == True:
            screen.blit(selectedAnwser, destinations[i])

    for i, state in enumerate(correctStates):
        if state == True:
            screen.blit(correctAnwser, destinations[i])

    for i, state in enumerate(selectedStatesLL):
        if state == True:
            screen.blit(usedLL, destinationsLL[i])

def drawLevels():
    #blit inidicator
    screen.blit(levelIndicator, (730, 360-(game.getLevel()*25)))
    #blit levels
    for i, level in enumerate(levels):
        screen.blit(level, (740, 360 -(i*25)))


def drawText(font: pg.font.Font, text: str, x: int, y: int, wrap: bool, wrapLen = 80, color="white"):
    if len(text) > wrapLen and wrap == True:
        textWrapped = ""
        textSplit = text.split(" ")
        for word in textSplit:
            if len(textWrapped.split("\n")[-1]) > wrapLen:
                textWrapped += "\n"
            textWrapped += word + " "
        text = textWrapped
    
    questionText = font.render(text, True, color)
    questionRect = questionText.get_rect(center=(x, y))
    screen.blit(questionText, questionRect)

# spillogik
game = Game()
popUpShown = False #options are 0:main and 1:popup
popUpType = None

def drawPopups(popUpType):
    if popUpType != None:
        global popUpShown, propabilities
        if popUpShown == True:
            screen.blit(popUp, (centerX-popUp.get_size()[0]/2+5, 85))
            closePopUpBtn.draw(screen)
            closePopUpBtn.checkPressed(screen)
            drawText(FONT1, "Continue Game", centerX-popUp.get_size()[0]/2+225, 352, False)

            if popUpType == "AA": #ask audience
                drawText(FONT0, "Ask the Audience", screen.get_width()/2, 98, False)
                drawText(FONT1, f"A: {propabilities[0]}%        B: {propabilities[1]}%        C: {propabilities[2]}%        D: {propabilities[3]}%", screen.get_width()/2, 300, False)
                for i, p in enumerate(propabilities):
                    pg.draw.rect(screen, (60, 120, 215), (250+i*111, 190+int(90-2.5*p), 70, int(p*2.5)))
                    selectedStatesLL[0] = True

            if popUpType == "AH": #ask host
                drawText(FONT0, "Ask the Host", centerX-popUp.get_size()[0]/2+225, 98, False)
                drawText(FONT0, hostAnswer, centerX-popUp.get_size()[0]/2+225, 190, True, 40)
                selectedStatesLL[1] = True
                
            if popUpType == "CF": #call friend
                drawText(FONT0, "Call a Friend", centerX-popUp.get_size()[0]/2+225, 98, False)
                drawText(FONT0, friendAnswer, centerX-popUp.get_size()[0]/2+225, 190, True, 40)
                selectedStatesLL[3] = True

suspenseCooldown = 0
revealCooldown = 0
cooldownDelta = FPS*5
guessWasCorrect = False

# lydsystem
sound = Sound()
sound.playMainMusic()
volume = 1
volumeDelta = 0.02
targetVolume = 0.25

ttsThread = threading.Thread(target=sound.tts, args=(game.getQuestion()["question"],), daemon=True)
ttsThread.start()


running = True
while running == True:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:  
            running = False

    screen.blit(bgImg, (0,0))
    drawWidgets()
    drawStates()
    drawLevels()
    drawPopups(popUpType)

    question = game.getQuestion()["question"]
    drawText(FONT0, question, 450, 530, True)

    options = game.getQuestion()["options"]
    drawText(FONT2, options[0], 265, 612, False)
    drawText(FONT2, options[1], 635, 612, False)
    drawText(FONT2, options[2], 265, 663, False)
    drawText(FONT2, options[3], 635, 663, False)

    drawText(FONT1, str(game.getLevel()+1), 448, 638, False)

    sound.setVolume(soundTgl.state*volume)
    if volume < targetVolume:
        volume = min(volume+volumeDelta, targetVolume)
    elif volume > targetVolume:
        volume = max(volume-volumeDelta, targetVolume)

    if sum(selectedStates) and suspenseCooldown + revealCooldown == 0:
        if game.getQuestion()["options"][selectedStates.index(True)] != "":
            drawStates()
            pg.display.update()
            sound.playSuspenseMusic()
            suspenseCooldown = cooldownDelta
        else:
            selectedStates = [False]*4
        
    if suspenseCooldown > 1:
        suspenseCooldown -= 1
    
    if suspenseCooldown == 1:
        suspenseCooldown -= 1
        sound.pauseMusic()
        if selectedStates[game.getQuestion()["answer"]]:
            correctStates = selectedStates.copy()
            selectedStates = [False]*4
            sound.playSoundCorrect()
            if game.getLevel() < 14:
                guessWasCorrect = True
                revealCooldown = cooldownDelta
            else:
                guessWasCorrect = False
                sound.playSoundWin()
                revealCooldown = 26*FPS
        else:
            correctStates[game.getQuestion()["answer"]] = True
            sound.playSoundWrong()
            guessWasCorrect = False
            selectedStatesLL = [False]*4
            revealCooldown = cooldownDelta
    
    if revealCooldown > 1:
        revealCooldown -= 1
    
    if revealCooldown == 1:
        revealCooldown -= 1

        if guessWasCorrect:
            game.nextLevel()
        else:
            game.gameOver()

        correctStates = [False]*4
        selectedStates = [False]*4

        sound.playMainMusic()
        targetVolume = 0.25
        ttsThread = threading.Thread(target=sound.tts, args=(game.getQuestion()["question"],), daemon=True)
        ttsThread.start()
    

    if suspenseCooldown + revealCooldown == 0:
        checkWidgets()

    if ttsThread.is_alive() == False:
        targetVolume = 1

    pygame_widgets.update(events) 
    pg.display.update()
    clock.tick(FPS)