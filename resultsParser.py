import re
from signalsample import SignalSample

class ResultsParser():

	samples = []

	def parseOutput(self, output, arguments):
		lines = output.splitlines()

		argumentsArray = arguments.split('|')
		sample = None

		for line in lines:
			tabPosition = line.find('\t')
			if tabPosition == -1:
				sample = self.createSignalSample(line)
			
			if sample is not None and line.count('\t') == 1:
				for index, argument in enumerate(argumentsArray):
					line = line.replace('\t', '')
					position = line.find(argument + ':')
					if position >= 0:
						if argument == 'SSID':
							sample.bssid = self.extractValue(line)
						if argument == 'freq':
							sample.frequency = self.extractValue(line)
						if argument == 'signal':
							sample.level = self.extractValue(line)
		
		return self.samples

	def createSignalSample(self, line):
		sample = SignalSample()
		sample.bssid = self.extractValue(line)
		self.samples.append(sample)
		return sample

	def extractValue(self, line):
		spacePosition = line.find(' ')
		bracketPosition = line.find('(')
		if bracketPosition == -1:
			bracketPosition = len(line)
		return line[(spacePosition + 1):bracketPosition].strip()
