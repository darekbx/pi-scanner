from scanner import Scanner
import zlib
import base64

scanner = Scanner()
resultJson = scanner.runScan()

print base64.b64encode(resultJson)