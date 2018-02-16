from scanner import Scanner
from bluepy.bluepy.btle import UUID, Peripheral

temp_uuid = UUID(0x2221)
p = Peripheral("A8:96:75:32:9D:EB", "random")

try:
	ch = p.getCharacteristics(uuid=temp_uuid)[0]
	if (ch.supportsRead()):
		while 1:
			value = ch.read()
			print str(val)

			#scanner = Scanner()
			#scanner.runScan()
			time.sleep(1)

finally:
    p.disconnect()