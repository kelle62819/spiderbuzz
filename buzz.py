import sys, hid, time, pygame
lights = []
debug = False
def deviceInit():
    "deviceInit establishes connections to the Buzz! controllers"
    devices = []
    for d in hid.enumerate(0x054c, 0x1000):
        dev = hid.device(0x054c, 0x1000, d["path"])
        dev.set_nonblocking(True)
        for i in range(0,10):
            dev.read(5)
        devices.append(dev)


        for x in range(0,4):
                lights.append(0x0)
    
    return devices

def getPress(devices):
    if debug:
        devcnt = 0;
        while 1:
            for event in pygame.event.get():           
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        return 0
                    if event.key == pygame.K_z:
                        return 1
                    if event.key == pygame.K_e:
                        return 2
                    if event.key == pygame.K_r:
                        return 3
                    if event.key == pygame.K_t:
                        return 4
                    if event.key == pygame.K_q:
                        return 5
                    if event.key == pygame.K_s:
                        return 6
                    if event.key == pygame.K_d:
                        return 7
                    if event.key == pygame.K_f:
                        return 8
                    if event.key == pygame.K_g:
                        return 9
                    if event.key == pygame.K_w:
                        return 10
                    if event.key == pygame.K_x:
                        return 11
                    if event.key == pygame.K_c:
                        return 12
                    if event.key == pygame.K_v:
                        return 13
                    if event.key == pygame.K_b:
                        return 14
                    if event.key == pygame.K_y:
                        return 15
                    if event.key == pygame.K_u:
                        return 16
                    if event.key == pygame.K_i:
                        return 17
                    if event.key == pygame.K_o:
                        return 18
                    if event.key == pygame.K_p:
                        return 19
                    if event.key == pygame.K_h:
                        return 20
                    if event.key == pygame.K_j:
                        return 21
                    if event.key == pygame.K_k:
                        return 22
                    if event.key == pygame.K_l:
                        return 23
                    if event.key == pygame.K_m:
                        return 24
                    if event.key == pygame.K_n:
                        return 25
                    if event.key == pygame.K_COMMA:
                        return 26
                    if event.key == pygame.K_SEMICOLON:
                        return 27
                    if event.key == pygame.K_COLON:
                        return 28
                    if event.key == pygame.K_EQUALS:
                        return 29

    else:
        while 1:
            devcnt=0
            for dev in devices:
                data = dev.read(5)
                if data is not None and len(data) > 2:
                    if data[3]== 128:
                        return devcnt
                    if data[4]== 248:
                        return devcnt+1
                    if data[4]== 244:
                        return devcnt+2
                    if data[4]== 242:
                        return devcnt+3
                    if data[4]== 241:
                        return devcnt+4
                    if data[3]== 4:
                        return devcnt+5
                    if data[3]== 64:
                        return devcnt+6
                    if data[3]== 32:
                        return devcnt+7
                    if data[3]== 16:
                        return devcnt+8
                    if data[3]== 8:
                        return devcnt+9
                    if data[2]== 32:
                        return devcnt+10
                    if data[3]== 2:
                        return devcnt+11
                    if data[3]== 1:
                        return devcnt+12
                    if data[2]== 128:
                        return devcnt+13
                    if data[2]== 64:
                        return devcnt+14
                    if data[2]== 1:
                        return devcnt+15
                    if data[2]== 16:
                        return devcnt+16
                    if data[2]== 8:
                        return devcnt+17
                    if data[2]== 4:
                        return devcnt+18
                    if data[2]== 2:
                        return devcnt+19

                devcnt=devcnt+20

def lightRun(devices):
        for dev in devices:
                dev.write([0x0,0x0,0x0,0x0,0x0,0xFF,0x0,0x0])
                time.sleep(0.2)
                dev.write([0x0,0x0,0x0,0x0,0xFF,0x0,0x0,0x0])
                time.sleep(0.2)
                dev.write([0x0,0x0,0x0,0xFF,0x0,0x0,0x0,0x0])
                time.sleep(0.2)
                dev.write([0x0,0x0,0xFF,0x0,0x0,0x0,0x0,0x0])
                time.sleep(0.2)
                dev.write([0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0])


        for light in lights:
                light=0x0

def light(devices,idx,on):
    if on:
        lights[idx]=0xFF
    else:
        lights[idx]=0x0
    lidx = idx-(idx%4)
    buff = [0x0,0x0,lights[lidx+3],lights[lidx+2],lights[lidx+1],lights[lidx],0x0,0x0]
    devices[idx//4].write(buff)


def release(devices):
    for dev in devices:
        dev.close()


        

def blink(devices,idx):
    for x in range(0,4):
        light(devices,idx,1)
        time.sleep(0.2)
        light(devices,idx,0)
        time.sleep(0.2)
    lights[idx]=0x0






                        
