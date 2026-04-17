import re
d=input()
b=d.split()[0]
e=[i.strip(",").strip(";") for i in d.split()[1:]]
v=[re.sub("[^a-zA-Z0-9 \n\.]", "", i) for i in d.split()[1:]]
for x,y in zip(e,v) :
 t=b
 t+=x.replace(y,"")[::-1].replace("][","[]")
 print(f"{t} {y};")