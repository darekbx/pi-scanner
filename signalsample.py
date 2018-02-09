class SignalSample():
	bss = ''
	ssid = ''
	freq = ''
	signal = ''

	def __init__(self):
		return

	def toString(self):
		return "%s\n%s\n%s\n%s\n" % (self.bss, self.ssid, self.freq, self.signal) 