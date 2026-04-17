l,c=input().split()
r,i=[],0
while len(r)!=int(l):
 i+=1
 if c in str(i):continue
 r+=[i]
print(r[-1])