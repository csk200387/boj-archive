import re
input()
d=input()
r=len(re.findall(r'R+',d))
f=len(re.findall(r'B+',d))
print([r+1,f+1][r>f])