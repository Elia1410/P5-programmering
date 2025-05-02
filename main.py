import pygame
import pygame_widgets
from pygame_widgets.button import Button

pygame.init()

screen = pygame.display.set_mode((900,700))
center = (screen.get_width()/2, screen.get_height()/2)
centerX = screen.get_width()/2 
centerY = screen.get_height()/2
pygame.display.set_caption("WWTBAM")

class NewButton: #new button temp
    def __init__(self, width, height, x, y, func):
        self.width = width
        self.height = height
        self.destX = x
        self.destY = y
        self.isHover = False
        self.func = func

    def checkHover(self):
        isHoverX = pygame.mouse.get_pos()[0] in list(range(self.destX, self.destX+self.width))
        isHoverY = pygame.mouse.get_pos()[1] in list(range(self.destY, self.destY+self.height))
        if isHoverX & isHoverY:
            self.isHover = True
            return self.isHover

    def checkPressed(self):
        if self.checkHover():
            pygame.event.get()
            if pygame.mouse.get_just_released()[0]:
               self.func()

    def drawEdges(self):
        pygame.draw.line(screen, "yellow", (self.destX, self.destY), (self.destX+self.width, self.destY+self.height), 3)
        pygame.draw.line(screen, "yellow", (self.destX, self.destY+self.height), (self.destX+self.width, self.destY), 3)


#Question box
question = Button(screen, 450, 532, 0, 0, text="What makes the moon “glow”?", textColour="white", textHAlign=center)

#Anwser buttons 
def selectedA():
    print("A Pressed")
def selectedB():
    print("B Pressed")
def selectedC():
    print("C Pressed")
def selectedD():
    print("D Pressed")
anwserA = NewButton(433-93, 632-593, 93, 593, selectedA)
answerC = NewButton(433-93, 682-643, 93, 643, selectedC)
anwserB = NewButton(800-460, 632-593, 460, 593, selectedB)
answerD = NewButton(800-460, 682-643, 460, 643, selectedD)
answerButtons = [anwserA, anwserB, answerC, answerD]


#text blit
    #level indicator
FONT1 = pygame.font.Font("ARIAL.TTF", size=20)
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

#image related
bgImg = pygame.image.load("pngs/background.png").convert()
correctAnwser = pygame.image.load("pngs/correct.png").convert_alpha()
correctAnwser.set_alpha(128)
selectedAnwser = pygame.image.load("pngs/selected.png").convert_alpha()
selectedAnwser.set_alpha(128)
destA, destB, destC, destD = (95, 592), (460, 592), (95, 642), (460, 642)

running = True
while running == True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:  
            running = False

    screen.fill((255,255,255))
    #draw background
    screen.blit(bgImg,(0,0))
    screen.blit(correctAnwser, destA)
    #blit levels
    for i,level in enumerate(levels):
        screen.blit(level, (740, 360 -(i*25)))

    for button in answerButtons:
        button.drawEdges()
        button.checkPressed()
    



    pygame_widgets.update(events) 
    pygame.display.update()
