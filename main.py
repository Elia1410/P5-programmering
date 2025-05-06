import pygame as pg
import pygame_widgets
from pygame_widgets.button import Button

from game import Game

pg.init()

screen = pg.display.set_mode((900,700))
center = (screen.get_width()/2, screen.get_height()/2)
centerX = screen.get_width()/2 
centerY = screen.get_height()/2
pg.display.set_caption("WWTBAM")
clock = pg.Clock()
FPS = 60

class Widget: #superclass
    def __init__(self, width, height, posX, posY, func, widgetImage, hoverImage):
        self.width = width
        self.height = height
        self.posX = posX
        self.posY = posY
        self.isHover = False
        self.func = func
        self.widgetImage = widgetImage
        self.hoverImage = hoverImage
        self.justPressed = False

    def drawEdges(self):
        pg.draw.line(screen, "yellow", (self.posX, self.posY), (self.posX + self.width, self.posY + self.height), 3)
        pg.draw.line(screen, "yellow", (self.posX, self.posY + self.height), (self.posX + self.width, self.posY), 3)


class Button(Widget): #subclass of Widget for buttons
    def __init__(self, width, height, posX, posY, func, widgetImage = None, hoverImage = None):
        super().__init__(width, height, posX, posY, func, widgetImage, hoverImage)
        self.buttonImage = widgetImage

    def draw(self):
        if self.buttonImage != None:
            screen.blit(self.buttonImage, (self.posX, self.posY))

    def checkHover(self):
        isHoverX = pg.mouse.get_pos()[0] in list(range(self.posX, self.posX+self.width))
        isHoverY = pg.mouse.get_pos()[1] in list(range(self.posY, self.posY+self.height))
        if isHoverX == True & isHoverY == True:
            self.isHover = True
            if self.hoverImage != None:
                screen.blit(self.hoverImage, (self.posX, self.posY))
            return self.isHover
    
    def checkPressed(self):
        if self.checkHover() == True:
            pg.event.get()
            if pg.mouse.get_pressed()[0]:
                if not self.justPressed:
                    self.func()
                    self.justPressed = True
            else: 
                self.justPressed = False

        
class Toggle(Widget): #subclass of Widget for toggles
    def __init__(self, width, height, posX, posY, state, widgetImages = None, hoverImages = None):
        super().__init__(width, height, posX, posY, func=None, widgetImage=None, hoverImage=None)
        self.state = state
        self.toggleImages = widgetImages
        self.hoverImages = hoverImages

    def draw(self):
        if self.toggleImages != None:
            if self.state == True:
                screen.blit(self.toggleImages[0], (self.posX, self.posY))
            else:
                screen.blit(self.toggleImages[1], (self.posX, self.posY))
    
    def checkHover(self):
        isHoverX = pg.mouse.get_pos()[0] in list(range(self.posX, self.posX+self.width))
        isHoverY = pg.mouse.get_pos()[1] in list(range(self.posY, self.posY+self.height))
        if isHoverX == True & isHoverY == True:
            self.isHover = True
            if self.hoverImages != None:
                if self.state == True:
                    screen.blit(self.hoverImages[0], (self.posX, self.posY))
                else:
                    screen.blit(self.hoverImages[1], (self.posX, self.posY))
            return self.isHover
        
    def checkPressed(self):
        if self.checkHover() == True:
            pg.event.get()
            if pg.mouse.get_pressed()[0]:
                if not self.justPressed:
                    if self.state == True:
                        self.state = False
                    else:
                        self.state = True
                    self.justPressed = True
            else: 
                self.justPressed = False
                
def checkWidgets():
    for w in widgets:
        w.draw()
        w.checkPressed()
    
#image related
bgImg = pg.image.load("pngs/background.png").convert()
askAudience = pg.transform.scale(pg.image.load("pngs/askaudience.png"), (85, 52)).convert()
askHost = pg.transform.scale(pg.image.load("pngs/askhost.png"), (85, 52)).convert()
fiftyFifty = pg.transform.scale(pg.image.load("pngs/5050.png"), (85, 52)).convert()
callFriend = pg.transform.scale(pg.image.load("pngs/call.png"), (85, 52)).convert()


    #anwser buttons
correctAnwser = pg.image.load("pngs/correct.png").convert_alpha()
correctAnwser.set_alpha(100)
selectedAnwser = pg.image.load("pngs/selected.png").convert_alpha()
selectedAnwser.set_alpha(100)
hoverAnwser = pg.image.load("pngs/selected.png").convert_alpha()
hoverAnwser.set_alpha(35)
disabledAnwser = pg.image.load("pngs/unavailable.png").convert_alpha()
disabledAnwser.set_alpha(80)
destA, destB, destC, destD = (93, 592), (460, 592), (93, 642), (460, 642)
destinations = [destA, destB, destC, destD]

    #lifeline buttons
usedLL = pg.transform.scale(pg.image.load("pngs/LLused.png"), (85, 52)).convert_alpha()
usedLL.set_alpha(80)
hoverLL = pg.transform.scale(pg.image.load("pngs/LLselected.png"), (85, 52)).convert_alpha()
hoverLL.set_alpha(50)
destAskAudience, destAskHost, dest5050, destCallFriend = (30, 125), (30, 190), (30, 255), (30, 320)
destinationsLL = [destAskAudience, destAskHost, dest5050, destCallFriend]

    #sound toggle
soundOn = pg.transform.scale(pg.image.load("pngs/sound on.png"), (int(83*0.75), int(74*0.75))).convert()
soundOff = pg.transform.scale(pg.image.load("pngs/sound off.png"), (int(83*0.75), int(74*0.75))).convert()
soundOnHover = pg.transform.scale(pg.image.load("pngs/sound on hover.png"), (int(83*0.75), int(74*0.75))).convert_alpha()
soundOnHover.set_alpha(80)
soundOffHover = pg.transform.scale(pg.image.load("pngs/sound off hover.png"), (int(83*0.75), int(74*0.75))).convert_alpha()
soundOffHover.set_alpha(80)

    #popup
popUp = pg.image.load("pngs/pop up image.png").convert()


#buttons
    #anwser buttons 
def selectedA():
    print("A Pressed")
    selectedStates[0] = True
def selectedB():
    print("B Pressed")
    selectedStates[1] = True
def selectedC():
    print("C Pressed")
    selectedStates[2] = True
def selectedD():
    print("D Pressed")
    selectedStates[3] = True

anwserBtnA = Button(433-93,  632-593, destA[0], destA[1], selectedA, hoverImage=hoverAnwser)
anwserBtnC = Button(433-93,  682-643, destC[0], destC[1], selectedC, hoverImage=hoverAnwser)
anwserBtnB = Button(800-460, 632-593, destB[0], destB[1], selectedB, hoverImage=hoverAnwser)
anwserBtnD = Button(800-460, 682-643, destD[0], destD[1], selectedD, hoverImage=hoverAnwser)

    #lifelines
def usedAskAudience():
    print("AA pressed")
    selectedStatesLL[0] = True
def usedAskHost():
    print("AH pressed")
    selectedStatesLL[1] = True
def used5050():
    print("5050 Pressed")
    selectedStatesLL[2] = True
def usedCallFriend():
    print("CF used")
    selectedStatesLL[3] = True

LLaskAudienceBtn = Button(85, 52, destAskAudience[0], destAskAudience[1], usedAskAudience, askAudience ,hoverLL)
LLaskHostBtn     = Button(85, 52, destAskHost[0],     destAskHost[1],     usedAskHost,     askHost     ,hoverLL)
LL5050Btn        = Button(85, 52, dest5050[0],        dest5050[1],        used5050,        fiftyFifty  ,hoverLL)
LLcallFriendBtn  = Button(85, 52, destCallFriend[0],  destCallFriend[1],  usedCallFriend,  callFriend  ,hoverLL)

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

def showStates():
    for i, state in enumerate(selectedStates):
        if state == True:
            screen.blit(selectedAnwser, destinations[i])

    for i, state in enumerate(selectedStatesLL):
        if state == True:
            screen.blit(usedLL, destinationsLL[i])

#text blit
    #level indicator
FONT0 = pg.font.Font("ARIAL.TTF", size=16)
FONT1 = pg.font.Font("ARIAL.TTF", size=20)
levels=[FONT1.render("1   $ 100", True, "orange"),
        FONT1.render("2   $ 200", True, "orange"),
        FONT1.render("3   $ 300", True, "orange"),
        FONT1.render("4   $ 500", True, "orange"),
        FONT1.render("5   $ 1.000", True, "white"),
        FONT1.render("6   $ 2.000", True, "orange"),
        FONT1.render("7   $ 4.000", True, "orange"),
        FONT1.render("8   $ 8.000", True, "orange"),
        FONT1.render("9   $ 16.000", True, "orange"),
        FONT1.render("10  $ 32.000", True, "white"),
        FONT1.render("11  $ 64.000", True, "orange"),
        FONT1.render("12  $ 125.000", True, "orange"),
        FONT1.render("13  $ 250.000", True, "orange"),
        FONT1.render("14  $ 500.000", True, "orange"),
        FONT1.render("15  $ 1.000.000", True, "white")]


def drawText(font: pg.font.Font, text: str, x: int, y: int, wrap: bool, wrapLen = 80, color="white"):
    if len(text) > wrapLen and wrap == True:
        textWrapped = ""
        textSplit = text.split(" ")
        for word in textSplit:
            if len(textWrapped.split("\n")[-1]) > 80:
                textWrapped += "\n"
            textWrapped += word + " "
        text = textWrapped
    
    questionText = font.render(text, True, color)
    questionRect = questionText.get_rect(center=(x, y))
    screen.blit(questionText, questionRect)


def update():
    checkWidgets()
    showStates()
    #blit levels
    for i, level in enumerate(levels):
        screen.blit(level, (740, 360 -(i*25)))


# spillogik
game = Game()
suspenseWait = FPS * 3


running = True
while running == True:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:  
            running = False

    screen.blit(bgImg, (0,0))
    update()

    question = game.getQuestion()["question"]
    drawText(FONT0, question, 450, 530, True)

    options = game.getQuestion()["options"]
    drawText(FONT0, options[0], 265, 612, False)
    drawText(FONT0, options[1], 635, 612, False)
    drawText(FONT0, options[2], 265, 663, False)
    drawText(FONT0, options[3], 635, 663, False)

    pygame_widgets.update(events) 
    pg.display.update()
    clock.tick(FPS)