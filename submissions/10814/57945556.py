memNum = int(input(""))
l = list()
for i in range(0,memNum):
    mem = input("").split(" ")
    l.append([int(mem[0]), mem[1]])

sd = sorted(l, reverse=False, key=lambda x:x[0])
for i in range(0, memNum):
    print(str(sd[i][0]) + " " + sd[i][1])