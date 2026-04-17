a,b,c=map(int,input().split())
N=int(input())
r=[0]*N
for i in range(N):
 for l in range(3):
  x,y,z=map(int,input().split())
  r[i]+=x*a+y*b+z*c
print(max(r))