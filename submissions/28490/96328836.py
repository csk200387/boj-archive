import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
arr = []
for _ in range(n):
    a, b = list(map(int, input().split()))
    arr.append(a*b)

print(max(arr))