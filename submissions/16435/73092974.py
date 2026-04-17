_,n=map(int,input().split())
a=sorted(map(int,input().split()))
for i in a:
 if i<=n:n+=1
print(n)