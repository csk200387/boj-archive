t=[[False]*100 for _ in range(100)]
for data in open(0) :
 a,b,c,d= map(int,data.split())
 for i in range(b,d):
  for l in range(a,c):
   t[i][l]=True
print(sum(table,[]).count(True))