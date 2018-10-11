import os
import json

from utils import Utils
from resultsParser import ResultsParser

class Scanner():

	frequencies = [2412,2417,2422,2427,2432,2437,2442,2447,2452,2457,2462,2467,2472,
	5180,5200,5220,5240,5260,5280,5300,5320,5500,5520,5540,5560,5580,5600,5620,5640,
	5660,5680,5700,5720,5745,5765,5785,5805,5825]
	searchArguments = "BSS|SSID|freq|signal"
	commandCosmose = "sudo iw dev wlp4s0 scan | egrep \"" + searchArguments + "\""
	commandPi = "sudo iw dev wlan0 scan | egrep \"" + searchArguments + "\""
	
	isForPI = True

	def runScan(self):
		fingerprintCount = 0
		uniqueSamples = []
		while (fingerprintCount < 30):
			start = Utils().getMillis()
			command = self.commandPi if self.isForPI else self.commandCosmose
			output = os.popen(command.format()).read()

			signalSamples = ResultsParser().parseOutput(output, self.searchArguments)
			# uniqueSamplesCount = 0
			
			# for s in signalSamples:
			# 	sameCount = 0
			# 	for c in uniqueSamples:
			# 		if s.bssid == c.bssid and s.ssid == c.ssid and s.frequency == c.frequency and s.level == c.level:
			# 			sameCount = sameCount + 1
			# 	if sameCount == 0:
			# 		uniqueSamples.append(s)
			
			# fingerprintCount = fingerprintCount + 1
			
			return json.dumps([ob.__dict__ for ob in signalSamples])
			#print "Fingerprints: %d, unique signal samples: %d" % (fingerprintCount, len(uniqueSamples))
			#self.printTimeDiff(start)

	def printTimeDiff(self, start):
		difference = Utils().getMillis() - start
		print "Scanning took %dms" % difference 