n=int(input())%1500000
a,b=0,1
for i in range(n-1):
 a,b=b,(a+b)%10**6
print(b)