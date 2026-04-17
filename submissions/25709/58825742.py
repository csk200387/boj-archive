n=int(input())
c=0
while n!=0:
 if n-1==0:
  c+=1
  break
 n=min(n-1,int(str(n).replace("1","")))
 c+=1
print(c)