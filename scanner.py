import os
import re
import time

class Scanner():

	command = "sudo iw dev wlp4s0 scan | egrep \"SSID\""

	def runScan(self):
		count = 0
		while (count < 2):
			start = self.getMillis()
			
			output = os.popen(self.command).read()
			print self.parseOutput(output)

			self.printTimeDiff(start)
			count = count + 1

	def parseOutput(self, output):
		return "\n" + re.sub('(?m)^\s+', '', output)

	def getMillis(self):
		return int(round(time.time() * 1000))

	def printTimeDiff(self, start):
		difference = self.getMillis() - start
		print "%dms" % difference 
