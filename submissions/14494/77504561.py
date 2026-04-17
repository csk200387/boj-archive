n,m = map(int, input().split())
dp = [[0]*(m+1) for i in range(n+1)]
dp[1][1] = 1
for x in range(2, n+1):
    for y in range(2, m+1):
        if x == 2:
            dp[x-1][y] = 1
        if y == 2:
            dp[x][y-1] = 1
        dp[x][y] = (dp[x-1][y] + dp[x][y-1] + dp[x-1][y-1]) % 1000000007
print(dp[n][m])