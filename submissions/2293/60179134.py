t, *arr=open(0)
n, k = map(int, t.split())
coin = [*map(int, arr)]
dp = [1] + [0] * k
for c in coin :
    for i in range(c, k+1) :
        dp[i] += dp[i-c]
print(dp[k])