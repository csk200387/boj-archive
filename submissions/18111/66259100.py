import sys
input = lambda:sys.stdin.readline().rstrip()

n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]

ans = 1e9

for i in range(257):
    low = 0
    high = 0
    for j in range(n):
        for k in range(m):
            if land[j][k] < i:
                low += i - land[j][k]
            else:
                high += land[j][k] - i
    if low > high + b:
        continue

    cnt = high * 2 + low

    if cnt <= ans:
        ans = cnt
        height = i

print(ans, height)