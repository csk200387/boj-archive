n = int(input())
dp = [[0] * 10 for i in range(n)]
dp[0] = [0] + [1]*9
for i in range(1, n):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for l in range(1, 9):
        dp[i][l] = dp[i-1][l-1] + dp[i-1][l+1]
print(sum(dp[n-1])%10**9)