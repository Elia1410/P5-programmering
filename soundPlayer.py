import pygame as pg
pg.init()


class Sound:
    def __init__(self):
        # lydeffekter:
        self.effectCorrect = pg.mixer.Sound('sounds/correct.wav')
        self.effectWrong = pg.mixer.Sound('sounds/wrong.wav')
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
        pg.mixer.music.unpause()
    
    def playMainMusic(self):
        pg.mixer.music.load(self.mainTheme)
        pg.mixer.music.play(-1)

    def playSuspenseMusic(self):
        pg.mixer.music.load(self.suspenseTheme)
        pg.mixer.music.play(-1)


if __name__ == "__main__":
    screen = pg.display.set_mode((400, 400))
    soundsystem = Sound()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        keys = pg.key.get_just_pressed()
        if keys[pg.K_q]:
            soundsystem.playSoundWin()
        if keys[pg.K_w]:
            soundsystem.playSoundCorrect()
        if keys[pg.K_e]:
            soundsystem.playSoundWrong()
        if keys[pg.K_r]:
            soundsystem.playSoundStartGame()
        if keys[pg.K_t]:
            soundsystem.playMainMusic()
        if keys[pg.K_y]:
            soundsystem.playSuspenseMusic()
        if keys[pg.K_z]:
            soundsystem.pauseMusic()
        if keys[pg.K_x]:
            soundsystem.unpauseMusic()

        