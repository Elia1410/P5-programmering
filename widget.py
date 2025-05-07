import pygame as pg

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

    def drawEdges(self, screen):
        pg.draw.line(screen, "yellow", (self.posX, self.posY), (self.posX + self.width, self.posY + self.height), 3)
        pg.draw.line(screen, "yellow", (self.posX, self.posY + self.height), (self.posX + self.width, self.posY), 3)

#####################################################################################################################################

class Button(Widget): #subclass of Widget for buttons
    def __init__(self, width, height, posX, posY, func, widgetImage = None, hoverImage = None,):
        super().__init__(width, height, posX, posY, func, widgetImage, hoverImage)
        self.buttonImage = widgetImage

    def draw(self, screen):
        if self.buttonImage != None:
            screen.blit(self.buttonImage, (self.posX, self.posY))

    def checkHover(self, screen):
        isHoverX = pg.mouse.get_pos()[0] in list(range(int(self.posX), int(self.posX+self.width)))
        isHoverY = pg.mouse.get_pos()[1] in list(range(int(self.posY), int(self.posY+self.height)))
        if isHoverX == True & isHoverY == True:
            self.isHover = True
            if self.hoverImage != None:
                screen.blit(self.hoverImage, (self.posX, self.posY))
            return self.isHover
    
    def checkPressed(self, screen):
        if self.checkHover(screen) == True:
            pg.event.get()
            if pg.mouse.get_pressed()[0]:
                if not self.justPressed:
                    self.func()

                    self.justPressed = True
            else: 
                self.justPressed = False
        
#####################################################################################################################################

class Toggle(Widget): #subclass of Widget for toggles
    def __init__(self, width, height, posX, posY, state, widgetImages = None, hoverImages = None):
        super().__init__(width, height, posX, posY, func=None, widgetImage=None, hoverImage=None)
        self.state = state
        self.toggleImages = widgetImages
        self.hoverImages = hoverImages

    def draw(self, screen):
        if self.toggleImages != None:
            if self.state == True:
                screen.blit(self.toggleImages[0], (self.posX, self.posY))
            else:
                screen.blit(self.toggleImages[1], (self.posX, self.posY))
    
    def checkHover(self, screen):
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
        
    def checkPressed(self, screen):
        if self.checkHover(screen) == True:
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