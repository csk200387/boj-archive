n=int(input())
if n==0:exit(print(0))
a,b=0,1
for i in range(n-1):a,b=b%1000000007,(a+b)%1000000007
print(b)