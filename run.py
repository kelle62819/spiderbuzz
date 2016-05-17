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
    while 1:
    	click = buzz.getPress(devices)
    	if click%5 == 0:  ## buzz button was clicked
    		clicker=click/5
    		sons.play("ringin.mp3")
    		buzz.light(devices,clicker,1)
    		time.sleep(4)
    		buzz.light(devices,clicker,0)
    		buzz.clearPresses(devices);
    			



if __name__ == '__main__': main()



