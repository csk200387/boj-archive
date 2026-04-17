import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
t = int(input())
arr = sorted(map(int, input().split()))
start, end = 0, n-1
r = 0
while start <= end:
    s = arr[start] + arr[end]
    if s == t:
        r += 1
    if s > t:
        end -= 1
    else:
        start += 1
print(r)