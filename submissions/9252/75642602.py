a=list(input())
b=list(input())
dp=[[""]*(len(b)+1)for i in range(len(a)+1)]
for x in range(1,len(a)+1):
 for y in range(1,len(b)+1):
  if a[x-1]==b[y-1]:dp[x][y]=dp[x-1][y-1]+a[x-1]
  else:dp[x][y]=max(dp[x-1][y],dp[x][y-1],key=len)
print(len(dp[-1][-1]))
print(dp[-1][-1])