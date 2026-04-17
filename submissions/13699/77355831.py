dp = [0] * 36
dp[0] = 1
n = int(input())
for i in range(1, n+1):
    tmp = 0
    for c in range(i):
        tmp += dp[c]*dp[i-c-1]
    dp[i] = tmp
print(dp[n])