from scanner import Scanner
import zlib
import base64

scanner = Scanner()
resultJson = scanner.runScan()
zipped = zlib.compress(resultJson)
print base64.b64encode(zipped)