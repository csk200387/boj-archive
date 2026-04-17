for n in open(0):
 r=0
 s,e=map(int,n.split())
 for i in range(s,e+1):
  t=set()
  b=True
  for j in str(i):
   if j in t:
    b=False
    break
   t.add(j)
  if b:r+=1
 print(r)