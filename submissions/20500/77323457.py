dp = [0, 1]
for i in range(int(input())-2):
 dp.append([(dp[-1]*2-1)%1000000007,(dp[-1]*2+1)%1000000007][i%2==0])
print(dp[-1])