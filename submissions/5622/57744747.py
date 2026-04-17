a=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"];r=0
for i in input() :
 for l in a :
  if i in l :
   r+=a.index(l)+3
print(r)