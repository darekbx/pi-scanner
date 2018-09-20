import os

from utils import Utils
from resultsParser import ResultsParser

class Scanner():

	frequencies = [2412,2417,2422,2427,2432,2437,2442,2447,2452,2457,2462,2467,2472,
	5180,5200,5220,5240,5260,5280,5300,5320,5500,5520,5540,5560,5580,5600,5620,5640,
	5660,5680,5700,5720,5745,5765,5785,5805,5825]
	searchArguments = "BSS|SSID|freq|signal"
	commandCosmose = "sudo iw dev wlp4s0 scan freq {0} | egrep \"" + searchArguments + "\""
	commandPi = "sudo iw dev wlan0 scan freq {0} | egrep \"" + searchArguments + "\""
	
	isForPI = True

	def runScan(self):
		fingerprintCount = 0
		uniqueSamples = []
		while (fingerprintCount < 30):
			start = Utils().getMillis()

			for frequency in self.frequencies:

				start1 = Utils().getMillis()
				command = self.commandPi if self.isForPI else self.commandCosmose
				output = os.popen(command.format(frequency)).read()

				# signalSamples = ResultsParser().parseOutput(output, self.searchArguments)
				# uniqueSamplesCount = 0
				
				# for s in signalSamples:
				# 	sameCount = 0
				# 	for c in uniqueSamples:
				# 		if s.bss == c.bss and s.ssid == c.ssid and s.freq == c.freq and s.signal == c.signal:
				# 			sameCount = sameCount + 1
				# 	if sameCount == 0:
				# 		uniqueSamples.append(s)
				
				print "{}".format(frequency)
				self.printTimeDiff(start1)
				fingerprintCount = fingerprintCount + 1
				
			print "Fingerprints: %d, unique signal samples: %d" % (fingerprintCount, len(uniqueSamples))
			self.printTimeDiff(start)

	def printTimeDiff(self, start):
		difference = Utils().getMillis() - start
		print "Scanning took %dms" % difference 

'''
scanning witch channel by frequency: sudo iw dev wlan0 scan freq 2412

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