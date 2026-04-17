import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.push(a*b)

print(max(arr))