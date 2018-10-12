import os
import json

from utils import Utils
from resultsParser import ResultsParser

class Scanner():

	searchArguments = "BSS|SSID|freq|signal"
	commandCosmose = "sudo iw dev wlp4s0 scan | egrep \"" + searchArguments + "\""
	commandPi = "sudo iw dev wlan0 scan | egrep \"" + searchArguments + "\""
	
	isForPI = False

	def runScan(self):
		command = self.commandPi if self.isForPI else self.commandCosmose
		output = os.popen(command.format()).read()
		signalSamples = ResultsParser().parseOutput(output, self.searchArguments)
		return json.dumps([ob.__dict__ for ob in signalSamples])