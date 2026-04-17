import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append(a)
    arr.append(b)

for i in range(n, 0, -1):
    if arr.count(i) == n:
        print(i)
        exit()
print(-1)