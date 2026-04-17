a=list(map(int,input().split()))
i=min(a)
while 1:
 t=0
 i+=1
 for n in a:
  if i%n==0:t+=1
 if t>=3:break
print(i)