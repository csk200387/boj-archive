input()
d = {}

for i in input():
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
arr = []
for i in "BSA":
    try:
        if d[i] == max(d.values()):
            arr.append(i)
    except KeyError:
        pass

if len(arr) == 3:
    print("SCU")
else:
    print(*arr, sep="")