import pygame
def init():
    pygame.mixer.init()

def play(sfile):
    pygame.mixer.music.load("sons/" + sfile)
    pygame.mixer.music.play()
