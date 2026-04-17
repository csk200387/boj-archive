import sys
input = lambda:sys.stdin.readline().rstrip()
n, a = map(int, input().split())
arr = [int(input()) for _ in range(n)]
start, end = 1, sum(arr)//a
while start <= end:
    cnt = 0
    t = (start+end)//2
    for i in arr:
        cnt += i//t
    if cnt >= a:
        start = t+1
    else:
        end = t-1
print(start-1)