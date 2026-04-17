n,*arr=open(0)
r=0
for i in arr:
    a,b=i.split()
    if a==b:r+=1
print(r if r else -1)