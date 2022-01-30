print("""
+--------------------------+
+ Python Headers  View     +
+  github.com/hawk-unity   +
+  instagram : coder.faruk +
+---------------------------
youtube: farukdeveloper.online
-------------------------------
- Http Header / Link Extractor
""")
#!/usr/bin/python3
import sys
from requests import get
url = input(" URL  (google.com)   ->   ")
response = get('https://api.hackertarget.com/httpheaders/?q=' + url).text
sys.stdout.write(response)
print("------------------------------LİNK EXTRACTOR---------------------------------------------------------->")
print("------------------------------LİNK EXTRACTOR---------------------------------------------------------->")
print("------------------------------LİNK EXTRACTOR---------------------------------------------------------->")
print("------------------------------LİNK EXTRACTOR---------------------------------------------------------->")
response2 = get('https://api.hackertarget.com/pagelinks/?q=' + url).text
