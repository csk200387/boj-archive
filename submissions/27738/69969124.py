n,x=int(input()),0
a,b,c,d,e,f=map(int,input().split())
for i in range(max(n-f,1),n+1):
 if i%a==0:x+=i
 if i%b==0:x%=i
 if i%c==0:x&=i
 if i%d==0:x^=i
 if i%e==0:x|=i
 if i%f==0:x>>=i
print(x)