import sys
input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

dp = [[0]*(m+1) for i in range(n+1)]
dp[1][1] = arr[0][0]

for x in range(1, n+1):
    for y in range(1, m+1):
        dp[x][y] = dp[x-1][y] + dp[x][y-1] + arr[x-1][y-1] - dp[x-1][y-1]

res = dp[1][1]

for x1 in range(1, n+1):
    for y1 in range(1, m+1):
        for x2 in range(x1, n+1):
            for y2 in range(y1, m+1):
                res = max(res, dp[x1-1][y2] + dp[x2][y1-1] + arr[x2-1][y2-1] - dp[x1-1][y1-1])

print(res)