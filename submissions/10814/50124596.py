import operator

memNum = int(input(""))
l = list()
for i in range(0,memNum):
    mem = input("").split(" ")
    l.append([mem[0], mem[1]])

sd = sorted(l, reverse=False, key=lambda x:x[0])

print(sd)
for i in range(0, len(sd)):
    print(sd[i][0] + " " + l[i][1])