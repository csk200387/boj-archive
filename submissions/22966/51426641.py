import sys
input = lambda:sys.stdin.readline().rstrip()
ar = {}
for _ in range(int(input())) :
    inp = input().split()
    title = inp[0]
    dif = int(inp[1])
    ar[title] = dif
print(sorted(ar.items(), key=lambda x: x[1])[0][0])