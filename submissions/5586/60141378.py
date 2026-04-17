import re

s = input()

pattern1 = re.compile(r'J(?=OI)')
matches1 = pattern1.findall(s)

pattern2 = re.compile(r'(?<=I)O(?=I)')
matches2 = pattern2.findall(s)

print(len(matches1))
print(len(matches2))