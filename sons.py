import pygame
def init():
    pygame.mixer.init()

def play(sfile):
    pygame.mixer.music.load("/home/pi/spiderbuzz/sons/" + sfile)
    pygame.mixer.music.play()
