a,b=open(0)
l=map(int,b.split())
t,c=0,0
for i in l:
 if t<=i:c+=1
 t=i
print(c)