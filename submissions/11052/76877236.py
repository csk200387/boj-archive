n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(1, n+1):
    for l in range(1, i+1):
        dp[i] = max(dp[i], arr[l] + dp[i-l])
print(dp)