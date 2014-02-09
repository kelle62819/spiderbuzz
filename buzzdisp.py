#!/usr/bin/env python
import pygame
screen = pygame.display.set_mode((1000,700))
def init():
    print "init"
    pygame.font.init()
    logo = pygame.image.load("img/logo.png")
    screen.fill((255,255,255))
    screen.blit(logo,(500-(logo.get_width()//2),160))
    pygame.display.flip()

def headline(str):
    header = pygame.Surface((1000,100))
    header.fill((255,255,255))
    font = pygame.font.SysFont("Helvetica",72)
    text = font.render(str,True,(255,132,0))
    screen.blit(header,(0,40))
    screen.blit(text,((1000-text.get_width())//2,40))
    pygame.display.flip()

def info(str):
    header = pygame.Surface((700,28))
    header.fill((255,255,255))    
    font = pygame.font.SysFont("Helvetica",20)
    text = font.render(str,True,(255,56,10))
    screen.blit(header,(150,520))
    screen.blit(text,((1000-text.get_width())//2,520))
    pygame.display.flip()

def camImage(webcam):
    back = pygame.Surface((600,315))
    back.fill((255,255,255))
    screen.blit(back,(200,160))
    webcam.start()
    img = webcam.get_image()
    image = pygame.Surface((240,240))
    image.blit(img,(0,0),(96,0,240,240))
    screen.blit(image,(380,160))
    pygame.display.flip()
    webcam.stop()
    return image

def bigImage(img):
    back = pygame.Surface((600,315))
    back.fill((255,255,255))
    screen.blit(back,(200,160))
    screen.blit(img,(500-(img.get_width()//2),160))
    pygame.display.flip()    

def addPlayer(img,idx):
    font = pygame.font.SysFont("Helvetica",20)
    newimg = pygame.transform.scale(img,(80,80))
    screen.blit(newimg,(100*idx,580))
    text = font.render("Joueur " + str(idx),True,(18,101,255))
    screen.blit(text,((100*idx)+40-(text.get_width()//2),550))
    text = font.render("0",True,(3,156,44))
    screen.blit(text,((100*idx)+40-(text.get_width()//2),662))
    pygame.display.flip()

def updateScores(playerImages, scores):
    font = pygame.font.SysFont("Helvetica",20)
    space = 820//(len(playerImages)-1)
    cnt = 0
    back = pygame.Surface((1000,150))
    back.fill((255,255,255))
    screen.blit(back,(0,550))
    for img in playerImages:
        newimg = pygame.transform.scale(img,(80,80))
        screen.blit(newimg,(cnt*space+50,580))
        text = font.render("Joueur " + str(cnt + 1),True,(18,101,255))
        screen.blit(text,((cnt*space+50)+40-(text.get_width()//2),550))
        text = font.render(str(scores[cnt]),True,(3,156,44))
        screen.blit(text,((cnt*space+50)+40-(text.get_width()//2),662))
        cnt= cnt+1
    pygame.display.flip()


def initLogo():
    return pygame.image.load("img/logo.png")
    
