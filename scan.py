from scanner import Scanner
import gzip
import base64
import StringIO

scanner = Scanner()
resultJson = scanner.runScan()
out = StringIO.StringIO()
with gzip.GzipFile(fileobj=out, mode="w") as f:
  f.write(resultJson)
zipped = out.getvalue()
print base64.b64encode(zipped)