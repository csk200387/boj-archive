dp = [0, 1, 1]
n = int(input())
for i in range(n-1):
 dp.append([(dp[-1]*2-1)%1000000007,(dp[-1]*2+1)%1000000007][i%2==0])
print(dp[n-1])