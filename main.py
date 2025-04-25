import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox

pygame.init()

screen = pygame.display.set_mode((900,700))
center = (screen.get_width()/2, screen.get_height()/2)
centerX = screen.get_width()/2 
centerY = screen.get_height()/2
pygame.display.set_caption("WWTBAM")

#Question box
question = TextBox(screen, 125, 500, 650, 40, )

#Anwser buttons
anwserA = Button(screen, 125, 600, 300, 30, text="A")
anwserB = Button(screen, 475, 600, 300, 30, text="B")
anwserC = Button(screen, 125, 650, 300, 30, text="C")
anwserD = Button(screen, 475, 650, 300, 30, text="D")

#image and rects
bgImg = pygame.image.load("background.png").convert()
"""
logoImg = pygame.image.load("logo.png").convert_alpha()
logoImg = pygame.transform.scale(logoImg, (300,300))
logoRect = logoImg.get_rect()
logoRect.center = (centerX,centerY-100)
"""


running = True
while running == True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:  
            running = False

    screen.fill((255,255,255))
    screen.blit(bgImg,(0,0))

    pygame_widgets.update(events) 
    pygame.display.update()
