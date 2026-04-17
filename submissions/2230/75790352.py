import sys
input = lambda:sys.stdin.readline().rstrip()
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
start, end = 0, n-1
t = arr[0] + arr[-1]
while start < end:
  s = arr[start] + arr[end]
  if t-s > m-s:
    t = s
  if s < m:
    start += 1
  else:
    end -= 1
print(t)