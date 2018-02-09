import os
import re

class Scanner():

	command = "sudo iw dev wlp4s0 scan | egrep \"SSID\""

	def runScan(self):
		count = 0
		while (count < 2):
			output = os.popen(self.command).read()
			print self.parseOutput(output)
			count = count + 1

	def parseOutput(self, output):
		return "\n" + re.sub('(?m)^\s+', '', output)
