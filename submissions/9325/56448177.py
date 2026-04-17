import sys
input = lambda:sys.stdin.readline().rstrip()

for _ in range(int(input())) :
    res = int(input())
    for i in range(int(input())) :
        a, b = map(int, input().split())
        res += a*b
    print(res)