import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
data = {}

for i in range(n):
    name, ring = input().split()
    if ring in data:
        data[ring].append(name)
    else:
        data[ring] = [name]
res = []
c = 0
for key in data:
    if len(data[key]) == 2 and key != "-":
        res.append("{0} {1}".format(data[key][0], data[key][1]))
        c += 1

print(c)
if res:
    print(*res, sep="\n")