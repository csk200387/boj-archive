dp = [0] * 1_000_001
dp[0:3]=1,2,4
for i in range(3, 1_000_001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1_000_000_009
for i in range(int(input())):
    n = int(input())
    print(dp[n-1])