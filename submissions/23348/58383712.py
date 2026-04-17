t=lambda:input().split();a,b,c=map(int,t());N=int(input());r=[0]*N
for i in range(N):
 for l in range(3):x,y,z=map(int,t());r[i]+=x*a+y*b+z*c
print(max(r))