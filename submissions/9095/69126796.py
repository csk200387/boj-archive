_,*lines=open(0)
dp=[0]*11
dp[0:3]=1,2,4
for i in range(3, 11):
 dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
for line in lines:
 n=int(line)-1
 print(dp[n])