import sys
input = lambda:sys.stdin.readline().rstrip()
arr = [0, 1, 0, 0]
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    arr[a], arr[b] = arr[b], arr[a]
print(arr.index(1))