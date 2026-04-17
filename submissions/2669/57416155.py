r=range;t=[[0]*100 for _ in r(100)]
for e in open(0) :
 a,b,c,d= map(int,e.split())
 for i in r(b,d):
  for l in r(a,c):
   t[i][l]=1
print(sum(t,[]).count(1))