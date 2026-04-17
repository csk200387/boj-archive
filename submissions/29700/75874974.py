import sys
n, m, k = map(int, input().split())
arr = [input() for i in range(n)]
cnt = 0
t = "0" * k
for i in range(n):
    start, end = 0, k
    while end <= m:
        if arr[i][start:end] == t:
            cnt += 1
        start += 1
        end += 1
print(cnt)