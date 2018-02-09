import os
import re

from utils import Utils

class Scanner():

	searchArguments = "BSS|SSID|freq|signal"
	ssidArguments = "SSID"
	commandCosmose = "sudo iw dev wlp4s0 scan | egrep \"" + ssidArguments + "\""
	commandPi = "sudo iw dev wlan0 scan | egrep \"" + ssidArguments + "\""
	
	isForPI = False

	def runScan(self):
		count = 0
		while (count < 2):
			start = Utils().getMillis()
			command = self.commandPi if self.isForPI else self.commandCosmose
			output = os.popen(command).read()
			print self.parseOutput(output)

			self.printTimeDiff(start)
			count = count + 1

	def parseOutput(self, output):
		return "\n" + re.sub('(?m)^\s+', '', output)

	def printTimeDiff(self, start):
		difference = Utils().getMillis() - start
		print "Scanning took %dms" % difference 
