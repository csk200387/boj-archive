n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for l in range(i+1):
        if l == 0:
            dp[i][l] = dp[i][l] + dp[i-1][l]
        elif l == len(dp[i])-1:
            dp[i][l] = dp[i][l] + dp[i-1][l-1]
        else:
            dp[i][l] = max(dp[i-1][l-1], dp[i-1][l]) + dp[i][l]
print(max(dp[n-1]))