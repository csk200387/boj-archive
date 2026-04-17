import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
d = {}
no = True
for i in range(n):
    name, ring = input().split()
    if ring in d:
        d[ring].append(name)
    else:
        d[ring] = [name]

for key, value in d.items():
    if key != "-" and len(value) == 2:
        print(*value)
        no = False

if no:
    print(0)