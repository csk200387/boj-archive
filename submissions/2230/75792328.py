import sys
input = lambda:sys.stdin.readline().rstrip()
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
start, end = 0, n-1
t = 2000000000
while start < end:
  diff = arr[end] - arr[start]
  if t > diff and diff >= m:
    t = min(diff, t)
  if diff < m:
    start += 1
  else:
    end -= 1
print(t)