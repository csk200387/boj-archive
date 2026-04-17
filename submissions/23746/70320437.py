import sys
input = lambda:sys.stdin.readline().rstrip()
d = {}
for i in range(int(input())):
    a, b = input().split()
    d[b] = a
res = "".join([d[i] for i in input()])
a, b = map(int, input().split())
print(res[a-1:b])