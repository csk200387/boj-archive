import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
plan = list(map(int, input().split()))
real = list(map(int, input().split()))
cnt = 0
for r, p in zip(real, plan):
    if r >= p:
        cnt += 1
print(cnt)