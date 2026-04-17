n,k,i=map(int,input().split())
s=0
while k!=i:
 k-=k//2
 i-=i//2
 s+=1
print(s)