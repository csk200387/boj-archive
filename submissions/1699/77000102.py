n = int(input())
dp = [i for i in range(n+1)]
for i in range(2, n+1):
    for j in range(1, i):
        t = j**2
        if t > i:
            break
        if dp[i] > dp[i-t] + 1:
            dp[i] = dp[i-t] + 1
print(dp[n])