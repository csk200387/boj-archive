import re
a = input()
print(min(len(re.findall('1+',a)), len(re.findall('0+',a))))