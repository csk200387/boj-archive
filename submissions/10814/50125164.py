memNum = int(input(""))
l = list()
for i in range(0,memNum):
    mem = input("").split(" ")
    l.append([mem[0], mem[1]])

sd = sorted(l, reverse=False, key=lambda x:x[0])
result = list()
for i in range(0, memNum):
    result.append(sd[i][0] + " " + sd[i][1])

print("\n".join(result))