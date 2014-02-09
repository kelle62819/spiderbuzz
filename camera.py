import pygame.camera
import pygame.image
import sys

def init():
	pygame.camera.init()

	cameras = pygame.camera.list_cameras()

	print "Using camera %s ..." % cameras[0]

	webcam = pygame.camera.Camera(cameras[0],(432,240))

	return webcam

