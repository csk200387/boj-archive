import re

data = input()
base = data.split()[0]

dec = [i.strip(",").strip(";") for i in data.split()[1:]]
var = [re.sub("[^a-zA-Z0-9 \n\.]", "", i) for i in data.split()[1:]]

for x, y in zip(dec, var) :
    t = base
    t += x.replace(y, "")[::-1].replace("][", "[]")
    print(f"{t} {y};")