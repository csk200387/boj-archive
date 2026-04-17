import sys
input = lambda:sys.stdin.readline().rstrip()
ar = [[*map(int, input().split())] for _ in range(int(input()))]
ar.sort(key=lambda x:(x[1], x[0]))
for x in ar :
    print(*x)