import pygame as pg
import pygame_widgets
from pygame_widgets.button import Button
from os import system

from DATA.game import Game

from DATA.audio.soundPlayer import Sound

import threading

pg.init()

screen = pg.display.set_mode((900,700))
center = (screen.get_width()/2, screen.get_height()/2)
centerX = screen.get_width()/2 
centerY = screen.get_height()/2
pg.display.set_caption("WWTBAM")
clock = pg.Clock()
FPS = 60

from DATA.GUI.assets import *
from DATA.GUI.widget import Button, Toggle
                
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

# liste af alle widgets
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

# til rendering af tekst på skærmen
def drawText(font: pg.font.Font, text: str, x: int, y: int, wrap: bool, wrapLen = 80, color="white"):
    """
    Tegner tekst på skærmen, centreret på (x, y) skærmposition
    """
    if len(text) > wrapLen and wrap == True:
        # "wrap" teksten, så en ny linje indsættes hvis teksten er længere end  wrapLen
        textWrapped = ""
        textSplit = text.split(" ")
        for word in textSplit:
            if len(textWrapped.split("\n")[-1]) > wrapLen:
                textWrapped += "\n"
            textWrapped += word + " "
        text = textWrapped
    
    # blit teksten på skærmen
    questionText = font.render(text, True, color)
    questionRect = questionText.get_rect(center=(x, y)) # tekst centreres på et Rect objekt
    screen.blit(questionText, questionRect)


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

# initialiser objekt til spil-logik
game = Game()

# værdier til spillogik
suspenseCooldown = 0 # tid efter valg af svar
revealCooldown = 0 # tid efter korrekt svar afsløres
cooldownDelta = FPS*5
guessWasCorrect = False

# init lydsystem
sound = Sound()
sound.playMainMusic()
volume = 1
volumeDelta = 0.02
targetVolume = 0.25

# start en seperat cpu-tråd med TTS, så det kører samtidig med spil-løkken
ttsThread = threading.Thread(target=sound.tts, args=(game.getQuestion()["question"],), daemon=True)
ttsThread.start()

# start spil-løkke
running = True
while running == True:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:  
            running = False # afslut spil-løkken

    # tegn baggrundsbillede hver frame
    screen.blit(bgImg, (0,0))

    
    drawWidgets() # tegn widgets i 'widgets'-listen
    
    drawStates() # tegn highlight på widgets for hover og selected
    
    drawLevels() # tegn niveauer til pengesummen

    drawPopups(popUpType) # hvis et popup vindue er aktivt, tegnes det

    # hent og tegn spørgsmål fra Game objekt
    question = game.getQuestion()["question"]
    drawText(FONT0, question, 450, 530, True, 75)

    # hent og tegn svarmuligheder fra Game objekt
    options = game.getQuestion()["options"]
    drawText(FONT2, options[0], 265, 612, False)
    drawText(FONT2, options[1], 635, 612, False)
    drawText(FONT2, options[2], 265, 663, False)
    drawText(FONT2, options[3], 635, 663, False)

    # hent og tegn det nuværende niveau fra Game objekt
    level = str(game.getLevel()+1)
    drawText(FONT1, level, 448, 638, False)

    # sæt spillets lydafspillerens volume, så det glider op eller ned ift. den ønskede lydstyrke
    sound.setVolume(soundTgl.state*volume)
    if volume < targetVolume:
        volume = min(volume+volumeDelta, targetVolume)
    elif volume > targetVolume:
        volume = max(volume-volumeDelta, targetVolume)

    # tjek om en valgmulighed er valgt. hvis en er valgt, evalueres svaret
    if sum(selectedStates) and suspenseCooldown + revealCooldown == 0:
        if game.getQuestion()["options"][selectedStates.index(True)] != "": # tjek at valget ikke er negeret af 50:50
            sound.playSuspenseMusic()
            suspenseCooldown = cooldownDelta # start cooldownperiode
        else:
            selectedStates = [False]*4 # reset valg
        
    if suspenseCooldown > 1: # så længe cooldown > 1, tælles den ned
        suspenseCooldown -= 1
    
    # når cooldown når 1, afsløres det korrekte svar
    if suspenseCooldown == 1:
        suspenseCooldown -= 1
        sound.pauseMusic()
        if selectedStates[game.getQuestion()["answer"]]: # tjek om spillerens valg er det korrekte svar
            correctStates = selectedStates.copy()
            selectedStates = [False]*4
            sound.playSoundCorrect()
            if game.getLevel() < 14: # tjek om det ikke er det sidste spørgsmål
                guessWasCorrect = True
                revealCooldown = cooldownDelta
            else:
                guessWasCorrect = False
                sound.playSoundWin()
                # giv correct-lydeffekten tid til at spille færdig før spillet fortsætter
                revealCooldown = 26*FPS
        else:
            # spilleren svarer forkert:
            correctStates[game.getQuestion()["answer"]] = True
            sound.playSoundWrong()
            guessWasCorrect = False
            selectedStatesLL = [False]*4
            revealCooldown = cooldownDelta
    
    # cooldown-periode til det korrekte svar afsløres
    if revealCooldown > 1:
        revealCooldown -= 1
    
    # svaret afsløres
    if revealCooldown == 1:
        revealCooldown -= 1

        # evaluer svaret
        if guessWasCorrect:
            game.nextLevel()
        else:
            game.gameOver()

        # reset tilstande for highligt af svar og valg
        correctStates = [False]*4
        selectedStates = [False]*4

        sound.playMainMusic()
        targetVolume = 0.25 # lydstyrken sænkes

        # ny CPU-tråd startes med TTS der læser næste spørgsmål op
        ttsThread = threading.Thread(target=sound.tts, args=(game.getQuestion()["question"],), daemon=True)
        ttsThread.start()
    
    # så længe ingen cooldown-periode er igang tjekkes widgets for click
    if suspenseCooldown + revealCooldown == 0:
        checkWidgets()

    # hæv lydstyrken hvis TTS ikke er aktiv
    if ttsThread.is_alive() == False:
        targetVolume = 1

    pygame_widgets.update(events) 
    pg.display.update()
    clock.tick(FPS)

pg.quit() # luk for spillet