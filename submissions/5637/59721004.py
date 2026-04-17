import sys,re
print(max(re.findall("[a-z+A-Z\-]+",sys.stdin.read()),key=len).lower())