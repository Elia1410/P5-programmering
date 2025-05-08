import pygame as pg
import pyttsx3

import sys
import os

try:
    PATH = sys._MEIPASS  # PyInstaller 
except AttributeError:
    PATH = os.path.abspath(".")

class Sound:
    """Objekt til styring af lydeffekter, musik og TTS (Text To Speech)"""
    def __init__(self):
        

        # lydeffekter:
        self.effectButton = pg.mixer.Sound(os.path.join(PATH,'DATA/audio/sounds/button.wav'))
        self.effectCorrect = pg.mixer.Sound(os.path.join(PATH,'DATA/audio/sounds/correct.wav'))
        self.effectWrong = pg.mixer.Sound(os.path.join(PATH,'DATA/audio/sounds/wrong.wav'))
        self.effectStartGame = pg.mixer.Sound(os.path.join(PATH,'DATA/audio/sounds/startGame.wav'))
        self.effectWin = pg.mixer.Sound(os.path.join(PATH,'DATA/audio/sounds/win.wav'))
    
        # musik:
        self.mainTheme = os.path.join(PATH,'DATA/audio/sounds/mainTheme.mp3')
        self.suspenseTheme = os.path.join(PATH,'DATA/audio/sounds/suspense.mp3')
        self.currectTrack = None

        # lydstyrke
        self.mainThemeVolume = 0.1
        self.suspenseThemeVolume = 0.8
        self.effectButtonVolume = 0.5
        self.effectCorrectVolume = 1
        self.effectWrongVolume = 1
        self.effectStartGameVolume = 1
        self.effectWinVolume = 1

        self.volume = 1
        self.setVolume(self.volume)

        # text-to-speech (pyttsx3)
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        self.engine.setProperty('rate', 150)

    def playSoundButton(self):
        self.effectButton.play()

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
        pg.mixer.music.set_volume(self.volume*self.mainThemeVolume)
        pg.mixer.music.play(-1)
        self.currectTrack = self.mainTheme

    def playSuspenseMusic(self):
        pg.mixer.music.load(self.suspenseTheme)
        pg.mixer.music.set_volume(self.volume*self.suspenseThemeVolume)
        pg.mixer.music.play(-1)
        self.currectTrack = self.suspenseTheme

    def setVolume(self, vol):
        self.volume = vol

        if self.currectTrack == self.mainTheme:
            pg.mixer.music.set_volume(vol*self.mainThemeVolume)
        else:
            pg.mixer.music.set_volume(vol*self.suspenseThemeVolume)
        self.effectButton.set_volume(vol*self.effectButtonVolume)
        self.effectCorrect.set_volume(vol*self.effectCorrectVolume)
        self.effectWrong.set_volume(vol*self.effectWrongVolume)
        self.effectStartGame.set_volume(vol*self.effectStartGameVolume)
        self.effectWin.set_volume(vol*self.effectWinVolume)

    def tts(self, text):
        if self.volume > 0:
            try:
                self.engine.stop()
            except:
                pass
            self.engine.say(text)
            self.engine.runAndWait()


# test af lydsystem
if __name__ == "__main__":

    pg.init()
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
        if keys[pg.K_SPACE]:
            soundsystem.setVolume(0)
        if keys[pg.K_b]:
            soundsystem.setVolume(1)
        if keys[pg.K_k]:
            soundsystem.tts("Hello World")