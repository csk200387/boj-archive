for n in map(int,open(0)):
 r=""
 for i in range(n+1):
  if i==0:r="-"
  else:r=r+" "*(3**(i-1))+r
 print(r)