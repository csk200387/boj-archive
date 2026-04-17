import sys, re
t = sys.stdin.read()
arr = re.findall("[a-z+A-Z\-]+", t)
print(max(arr, key=len))