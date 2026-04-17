for n in open(0):
 r=""
 for i in range(int(n)+1):
  if i==0:r="-"
  else:r=r+" "*(3**(i-1))+r
 print(r)