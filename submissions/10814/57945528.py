import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
l = []
for i in range(n) :
    t, s = input().split()
    l.append([int(t), s])

for i in sorted(l, reverse=0, key=lambda x:x[0]) :
    print(*i)