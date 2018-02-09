import os

from utils import Utils
from resultsParser import ResultsParser

class Scanner():

	searchArguments = "BSS|SSID|freq|signal"
	commandCosmose = "sudo iw dev wlp4s0 scan | egrep \"" + searchArguments + "\""
	commandPi = "sudo iw dev wlan0 scan | egrep \"" + searchArguments + "\""
	
	isForPI = True

	def runScan(self):
		count = 0
		while (count < 1):
			start = Utils().getMillis()
			command = self.commandPi if self.isForPI else self.commandCosmose
			output = os.popen(command).read()

			signalSamples = ResultsParser().parseOutput(output, self.searchArguments)
			print "Samples count: %d\n" % len(signalSamples)

			for sample in signalSamples:
				print sample.toString()

			self.printTimeDiff(start)
			count = count + 1

	def printTimeDiff(self, start):
		difference = Utils().getMillis() - start
		print "Scanning took %dms" % difference 
