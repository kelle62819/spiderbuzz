#!/usr/bin/env python

import sys, usb.core, time
import buzz, sons
sons.init()


players = []
wrong = []
#MOdes: 0=Initialized, 1=Registration, 2:Game Mode, 3:In question
mode=0

#initialize buzz controls
devices=buzz.deviceInit()
sons.play("generique.mp3")
buzz.lightRun(devices)
##buzz.lightRun(devices)
##buzz.lightRun(devices)
##buzz.lightRun(devices)
##
##time.sleep(10)


print "Welcome to Spider Buzz!"
print "Hit Buzz! button to designate the host controller"

while 1:
	click = buzz.getPress(devices)
	if click%5 == 0:  ## buzz button was clicked
                #light up buzz button
		print "Press yellow button on host controller to confirm"
		if buzz.getPress(devices) == click+4:
			break
		print "Hit Buzz! button to designate the host controller"
mode=1
print "Registration is open"

while len(players)<7:
	print "Player " + str(len(players)+1) + ", click your Buzz! button to register"
	print "(the host may end registration by clicking the yellow button)"
	while 1:
		click = buzz.getPress(devices)
		if click == 4:
			break
		if click % 5 == 0 and click != 0:
			pNum = click / 5
			if not pNum in players:
				players.append(pNum)
				break
	if click == 4:
		break
mode=2	
print "Registration CLOSED"
print "Host can click next question button to start the game!"


while 1:
	while buzz.getPress(devices) != 1:
		test=1
	mode=3
	sons.play("zero.mp3")
	print "NEW QUESTION...."
	clicker = 0
	wrong = []
	while 1:
		click = buzz.getPress(devices)
		if click%5 == 0 and click != 0: #Player buzzed in
			clicker = click/5
			#If Player has already answered wrong their Buzz is not accepted
			if not clicker in wrong and clicker in players:
				pIndex = players.index(clicker)
				sons.play("ringin.mp3")
				print "Player " + str(pIndex+1) + " buzzed in first"
				#Wait for right or wrong decision
				while 1:
					click = buzz.getPress(devices)
					if click == 3:
						sons.play("wrong.mp3")
						print "WRONG ANSWER"
						wrong.append(clicker)
						break
					if click == 2:
						sons.play("right.mp3")
						print "RIGHT ANSWER!"
						wrong.append(clicker)
						break
					if click == 1:
						break
						
		if click == 1 or click == 2:  #Next Question button
			break	

