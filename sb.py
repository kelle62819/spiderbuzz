#!/usr/bin/env python
# coding=utf-8
import time, buzzdisp, buzz, sons, pygame, camera
from pygame.locals import *
round = 0

def main():
    sound=True
    
    buzzdisp.init()
    buzzdisp.headline("Spider Buzz!")
    logo = buzzdisp.initLogo()

    players = []
    wrong = []
    host = 0
    playerImages=[]
    scores=[]

    #initialize buzz controls
    devices=buzz.deviceInit()
    if sound:
        sons.init()
        sons.play("generique.mp3")

    buzz.lightRun(devices)
    buzz.lightRun(devices)

    buzzdisp.info("Maitre de jeu: Appuyez sur votre bouton rouge")


    while 1:

        click = buzz.getPress(devices)
        if click%5 == 0:  ## buzz button was clicked
            host = click//5
            buzz.light(devices,host,1)
            buzzdisp.info("Maitre de jeu: Appuyez sur votre bouton orange pour confirmer")
            if buzz.getPress(devices) == click+2:
                buzz.blink(devices,host)
                buzz.light(devices,host,1)

                break
            buzz.light(devices,host,0)
            buzzdisp.info("Maitre de jeu: Appuyez sur votre bouton rouge")
    mode=1
    
    buzzdisp.headline("Inscriptions")
    webcam = camera.init()

    while len(players)<(len(devices)*4)-1:
        while 1:
            buzzdisp.info("Joueur " + str(len(players)+1) + ", mettez vous devant la camera et appuyez sur votre bouton rouge")       
            buzzdisp.bigImage(logo)
            click = buzz.getPress(devices)
            if click == (host*5)+4:
                break
            if click % 5 == 0 and click != host*5:
                pNum = click // 5
                if not pNum in players:
                    if sound:
                        sons.play("camera.aiff")
                    img = buzzdisp.camImage(webcam)
                    buzzdisp.info("Appuyez sur le bouton orange pour accepter ou le bouton vert pour continuer")
                    while 1:
                        confclick = buzz.getPress(devices)
                        if confclick == pNum*5+2:
                            playerImages.append(img)
                            players.append(pNum)
                            scores.append(0)
                            buzz.light(devices,pNum,1)
                            buzzdisp.addPlayer(img,len(players))

                            break
                        if confclick == pNum*5+3:
                            break
                    if  confclick == pNum*5+2:
                        break  
        if click == (host*5)+4:
            break

    buzz.lightRun(devices)
    buzzdisp.updateScores(playerImages, scores)
    buzzdisp.headline("Les inscriptions sont closes")
    buzzdisp.info("Maitre: Appuyez sur le bouton bleu pour demarrer le jeu")


    while 1:
        while buzz.getPress(devices) != host*5+1:
            test=1
        
        if sound:
            sons.play("zero.mp3")
        buzzdisp.headline("Nouvelle question....")
        buzzdisp.info("")
        buzzdisp.bigImage(logo)
        buzz.lightRun(devices)
        clicker = 0
        wrong = []
        while 1:
            click = buzz.getPress(devices)
            if click%5 == 0 and click != host*5: #Player buzzed in
                clicker = click/5
                #If Player has already answered wrong their Buzz is not accepted
                if not clicker in wrong and clicker in players:
                    pIndex = players.index(clicker)
                    if sound:
                        sons.play("ringin.mp3")
                    buzz.light(devices,clicker,1)
                    buzzdisp.bigImage(playerImages[pIndex])
                    buzzdisp.headline("Joueur " + str(pIndex+1))
                    #Wait for right or wrong decision
                    while 1:
                        click = buzz.getPress(devices)
                        if click == host*5+3:
                            if sound:
                                sons.play("wrong.mp3")
                            buzzdisp.headline("MAUVAISE REPONSE")
                            wrong.append(clicker)
                            buzz.light(devices,clicker,0)

                            break
                        if click == host*5+2:
                            if sound:
                                sons.play("right.mp3")
                            buzzdisp.headline("BONNE REPONSE!")
                            scores[pIndex] = scores[pIndex] + 100
                            buzzdisp.updateScores(playerImages, scores)
                            buzz.light(devices,clicker,0)
                            break
                        if click == host*5+1:
                            break
                            
            if click == host*5+1 or click == host*5+2:  #Next Question button
                break   

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                buzz.release(devices)
                return
        pass

if __name__ == '__main__': main()
