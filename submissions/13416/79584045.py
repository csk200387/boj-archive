import sys
input = lambda:sys.stdin.readline().rstrip()
for c in range(int(input())):
    n = int(input())
    r = 0
    for i in range(n):
        r += max(0, *map(int, input().split()))
    print(r)