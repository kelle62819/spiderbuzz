import buzz

devices=buzz.deviceInit()

buzz.lightRun(devices)

for i in range(0,4):
	print buzz.getPress(devices)

for dev in devices:
	dev.close()

