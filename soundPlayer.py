import pygame as pg

class Sound:
    def __init__(self):
        # lydeffekter:
        self.effectCorrect = pg.mixer.Sound('sounds/correct.wav')
        self.effectWrong = pg.mixer.Sound('sounds/correct.wav')
        self.effectStartGame = pg.mixer.Sound('sounds/startGame.wav')
        self.effectWin = pg.mixer.Sound('sounds/win.wav')
    
        # musik:
        self.mainTheme = 'sounds/mainTheme.mp3'
        self.suspenseTheme = 'sounds/suspense.mp3'
    
    def playSoundCorrect(self):
        self.effectCorrect.play()

    def playSoundWrong(self):
        self.effectWrong.play()
    
    def playSoundStartGame(self):
        self.effectStartGame.play()

    def playSoundWin(self):
        self.effectWin.play()
    
    def pauseMusic(self):
        pg.mixer.music.pause()

    def unpauseMusic(self):
        pg.mixer.music.pause()
    
    def playMainMusic(self):
        pg.mixer.music.load(self.mainTheme)
        pg.mixer.music.play(-1)

    def plauSuspenseMusic(self):
        pg.mixer.music.load(self.suspenseTheme)
        pg.mixer.music.play(-1)