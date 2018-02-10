import os

from utils import Utils
from resultsParser import ResultsParser

class Scanner():

	searchArguments = "BSS|SSID|freq|signal"
	commandCosmose = "sudo iw dev wlp4s0 scan | egrep \"" + searchArguments + "\""
	commandPi = "sudo iw dev wlan0 scan freq 2412 | egrep \"" + searchArguments + "\""
	
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

'''

                        * 2412 MHz [1] (20.0 dBm)
                        * 2417 MHz [2] (20.0 dBm)
                        * 2422 MHz [3] (20.0 dBm)
                        * 2427 MHz [4] (20.0 dBm)
                        * 2432 MHz [5] (20.0 dBm)
                        * 2437 MHz [6] (20.0 dBm)
                        * 2442 MHz [7] (20.0 dBm)
                        * 2447 MHz [8] (20.0 dBm)
                        * 2452 MHz [9] (20.0 dBm)
                        * 2457 MHz [10] (20.0 dBm)
                        * 2462 MHz [11] (20.0 dBm)
                        * 2467 MHz [12] (20.0 dBm)
                        * 2472 MHz [13] (20.0 dBm)
                        * 2484 MHz [14] (disabled)
'''