import re
print(max(re.findall("[a-z+A-Z\-]+",open(0).read()),key=len).lower())