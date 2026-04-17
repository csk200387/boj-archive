import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    for _ in range(b):
        input()
    print(a-1)