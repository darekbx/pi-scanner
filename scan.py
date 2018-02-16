from scanner import Scanner
import pygatt

adapter = pygatt.BGAPIBackend()

try:
	adapter.start()
	device = adapter.connect('A8:96:75:32:9D:EB')
	while 1:
		value = device.char_read("00001105-0000-1000-8000-00805f9b34fb")
		print str(val)
		time.sleep(1)

finally:
    adapter.stop()

#scanner = Scanner()
#scanner.runScan()