import operator

memNum = int(input(""))
d = dict()
for i in range(0,memNum):
    mem = input("").split(" ")
    d[mem[1]] = int(mem[0])

sd = sorted(d.items(), reverse=False, key=lambda x:x[1])

for key, value in sd:
    print(key + " " + str(value))