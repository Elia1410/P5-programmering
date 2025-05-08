import pygame as pg

class Widget:
    """Superklasse/Overklasse til udvikling af subklasse widgets, som f.eks. Button eller Toggle.
    """
    def __init__(self, width, height, posX, posY, func, widgetImage, hoverImage):
        """Initialisering af widget parametre.
        Args:
            width (_int_): Bredde af widget.
            height (_int_): Højde af widget.
            posX (_int_): X-værdien af widget posistion koordinat (x, y), placeringen på skærmen i x-aksen.
            posY (_int_): Y-værdien af widget posistion koordinat, (x, y), placeringen på skærmen i y-aksen.
            func (_function_): Funktion der kaldes gennem widget, f.eks. ved klik.
            widgetImage (_pygame.Surface_): Billedet, der vises når widgetten er i normal tilstand (ikke hovered).
            hoverImage (_pygame.Surface_): Billedet, der vises når musen holdes over widgetten (hover-tilstand).
        """        
        self.width = width
        self.height = height
        self.posX = posX
        self.posY = posY
        self.isHover = False
        self.func = func
        self.widgetImage = widgetImage
        self.hoverImage = hoverImage
        self.justPressed = False # Boolsk variabel til at sikre at widgets kun trykkes på en gang

    def drawEdges(self, screen):
        """Tegner et kryds over widgettens interagerbare område, bruges hvis der intet widget-billede er tegnet endnu.
        Args:
            screen (_pygame.Surface_): Den surface som krydset tegnes på, typisk en window-surface.
        """        
        pg.draw.line(screen, "yellow", (self.posX, self.posY), (self.posX + self.width, self.posY + self.height), 3) # Linje fra top-venstre til bund-højre
        pg.draw.line(screen, "yellow", (self.posX, self.posY + self.height), (self.posX + self.width, self.posY), 3) # Linje fra bund-venstre til top-højre

#####################################################################################################################################

class Button(Widget):
    """En underklasse til opretning af knapper/buttons, der bruger billeder til udseende.
    Args:
        Widget (_class_): Superklassen som Button klassen arver argumenter(klasse parametre) og metoder fra.
    """    
    def __init__(self, width, height, posX, posY, func, widgetImage = None, hoverImage = None,): 
        super().__init__(width, height, posX, posY, func, widgetImage, hoverImage)

    def draw(self, screen: pg.Surface):
        """Tegner/blitter widgetImage billedet til knappen
        Args:
            screen (_pygame.Surface_): Den surface som billedet tegnes på, typisk en window-surface.
        """
        if self.widgetImage != None:
            screen.blit(self.widgetImage, (self.posX, self.posY))

    def checkHover(self, screen: pg.Surface):
        """Tjekker om musen er over knappen og tegner hoverImage, når det er sandt.
        Args:
            screen (_pygame.Surface_): Den surface som knappen er tegnet på, typisk en window-surface.
        Returns:
            bool: Sandt/falsk om musen er over knappen.
        """        
        isHoverX = pg.mouse.get_pos()[0] in list(range(int(self.posX), int(self.posX+self.width)))  # Tjeker om musen er inden for knappens område på x-aksen
        isHoverY = pg.mouse.get_pos()[1] in list(range(int(self.posY), int(self.posY+self.height))) # Tjeker om musen er inden for knappens område på y-aksen
        if isHoverX == True & isHoverY == True:
            self.isHover = True
            if self.hoverImage != None: # Hvis der er et hoverbillede tilhørende knappen, tegnes det på skærmen
                screen.blit(self.hoverImage, (self.posX, self.posY))
            return self.isHover
    
    def checkPressed(self, screen: pg.Surface):
        """Tjekker om knappen er blevet trykket på og kalder den tilhørende funktion.
        Args:
            screen (_pygame.Surface_): Den surface som knappen er tegnet på, typisk en window-surface.
        """        
        if self.checkHover(screen) == True: # Kun hvis musen er over knappen, kan den trykkes på
            pg.event.get()
            if pg.mouse.get_pressed()[0]: # Indexet [0] refferer til venstre-klik på musen
                if not self.justPressed: 
                    self.func()           # Funktionen kaldes kun en gang per klik, da justPressed boolen opdateres og forhindre næste iteration.
                    self.justPressed = True
            else: 
                self.justPressed = False
        
#####################################################################################################################################

class Toggle(Widget): # subklasse widget for toggles
    """En underklasse til opretning af toggles/kontakter, der bruger billeder til udseende.
    Args:
        Widget (_class_): Superklassen som Toggle klassen arver argumenter(klasse parametre) og metoder fra.
    """    
    def __init__(self, width, height, posX, posY, state, widgetImages = None, hoverImages = None): 
        super().__init__(width, height, posX, posY, func=None, widgetImage=None, hoverImage=None)
        self.state = state
        self.toggleImages = widgetImages # Har som forskel til superklassen Widget, 2 widgetimages og 2 hoverimages.
        self.hoverImages = hoverImages   # dette er skyldet at Toggle widgetten har 2 tilstande, hvor en ordinær Widget kun har 1.

    def draw(self, screen: pg.Surface):
        """Tegner/blitter det widgetImage billede der hører til kontaktens nuværende tilstand.
        Args:
            screen (_pygame.Surface_): Den surface som kontakten er tegnes på, typisk en window-surface.
        """        
        if self.toggleImages != None:
            if self.state == True:
                screen.blit(self.toggleImages[0], (self.posX, self.posY)) # Tegner billedet til tilstand 1
            else:
                screen.blit(self.toggleImages[1], (self.posX, self.posY)) # Tegner billedet til tilstand 2
    
    def checkHover(self, screen: pg.Surface):
        """Tjekker om musen er over knappen og tegner det hoverImage der hører til kontaktens tilstand, når det er sandt.
        Args:
            screen (_pygame.Surface_): Den surface som kontakten er tegnet på, typisk en window-surface.
        Returns:
            bool: Sandt/falsk om musen er over kontakten.
        """          
        isHoverX = pg.mouse.get_pos()[0] in list(range(self.posX, self.posX+self.width))  # Tjeker om musen er inden for knappens område på x-aksen
        isHoverY = pg.mouse.get_pos()[1] in list(range(self.posY, self.posY+self.height)) # Tjeker om musen er inden for knappens område på y-aksen
        if isHoverX == True & isHoverY == True:
            self.isHover = True
            if self.hoverImages != None: # Hvis der er et hoverbillede tilhørende knappen, tegnes det på skærmen
                if self.state == True: 
                    screen.blit(self.hoverImages[0], (self.posX, self.posY)) # Billede til tilstand 1
                else:
                    screen.blit(self.hoverImages[1], (self.posX, self.posY)) # Billede til tilstand 1
            return self.isHover
        
    def checkPressed(self, screen: pg.Surface):
        """Tjekker om kontakten er blevet trykket på og skifter kontaktens tilstand.
        Args:
            screen (_pygame.Surface_): Den surface som kontakten er tegnet på, typisk en window-surface.
        """     
        if self.checkHover(screen) == True: # Kun hvis musen er over knappen, kan den trykkes på
            pg.event.get()
            if pg.mouse.get_pressed()[0]: # Indexet [0] refferer til venstre-klik på musen
                if not self.justPressed:  # tilstanden ændres kun en gang per klik, da justPressed boolen opdateres og forhindre næste iteration.
                    if self.state == True:        
                        self.state = False  # Hvis kontakten er i tilstand 1, ændres den til 2, (f.eks. on)
                    else:
                        self.state = True
                    self.justPressed = True # Hvis kontakten er i tilstand 2, ændres den til 1, (f.eks. off)
            else: 
                self.justPressed = False