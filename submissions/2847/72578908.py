n,*a=map(int,open(0))
r=0
for i in range(n-1,0,-1):
 if a[i]<=a[i-1]:
  r+=a[i-1]-a[i]+1
  a[i-1]=a[i]-1
print(r)