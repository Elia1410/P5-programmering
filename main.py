import pygame

pygame.init()

pygame.display.set_mode((900,700))
pygame.display.set_caption("WWTBAM")

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
