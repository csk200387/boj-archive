import sys
input = lambda:sys.stdin.readline().rstrip()
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
start, end = 0, 0
t = 2000000000
while start < n and end < n:
  diff = arr[end] - arr[start]
  if diff < m:
    start += 1
  else:
    t = min(diff, t)
    end += 1
print(t)