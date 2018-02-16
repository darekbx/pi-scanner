import os
import time

def scan():
	start = getMillis()
	command = "sudo iw dev wlan0 scan | egrep \"BSS|SSID|freq|signal\""
	output = os.popen(command).read()
	print "%dms" % (getMillis() - start)

def getMillis():
	return int(round(time.time() * 1000))

scan()