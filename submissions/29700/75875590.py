import sys
input = lambda:sys.stdin.readline().rstrip()
n, m, k = map(int, input().split())
cnt = 0
t = "0" * k
for i in range(n):
    d = input().split('1')
    for i in d:
        if len(i) >= k:
            cnt += len(i) - k + 1
print(cnt)