a = list(input())
b = list(input())
c = list(input())
dp = [[[0]*(len(b)+1) for i in range(len(a)+1)] for j in range(len(c)+1)]
for i in range(1, len(c)+1):
    for j in range(1, len(a)+1):
        for k in range(1, len(b)+1):
            if a[j-1] == b[k-1] == c[i-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
print(dp[-1][-1][-1])