e,n=map(int,input().split())
a=sorted([int(input()) for i in range(n)],reverse=1)
R=[]
for c in a:
 t=[c for i in a if c <= i]
 if len(t)>e:break
 R.append(t)
r=max(R,key=sum)
print(r[0],sum(r))