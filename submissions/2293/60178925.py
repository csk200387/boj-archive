t, *arr = open(0)
n, k = map(int, t.split())
coins = [*map(int, arr)]
dp = [1] + [0] * k
for c in coins[::-1] :
    for i in range(c, k+1) :
        dp[i] += dp[i-c]

print(dp[k])