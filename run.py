#!/usr/bin/env python
# coding=utf-8
import time, buzz, sons

round = 0

def main():
    sound=True
    
    devices=buzz.deviceInit()
    if sound:
        sons.init()
        sons.play("generique.mp3")

    buzz.lightRun(devices)
    buzz.lightRun(devices)
    buzz.lightRun(devices)
    buzz.lightRun(devices)
    while 1:
    	click = buzz.getPress(devices)
    	if click%5 == 0:  ## buzz button was clicked
    		clicker=click/5
    		sons.play("ringin.mp3")
    		buzz.light(devices,clicker,1)
    		time.sleep(5)
    		buzz.light(devices,clicker,0)
    		buzz.clearPresses(devices);
    	if click%5 == 4:  ## yellow button was clicked
            sons.play("dingdong.mp3")
        if click%5 == 3:  ## green button was clicked
            sons.play("right.mp3")
        if click%5 == 2:  ## orange button was clicked
            sons.play("wrong.mp3")
        if click%5 == 1:  ## blue button was clicked
            sons.play("generique.mp3")
            buzz.lightRun(devices)
            buzz.lightRun(devices)
            buzz.lightRun(devices)
            buzz.lightRun(devices)


if __name__ == '__main__': main()



