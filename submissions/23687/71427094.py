n,*r=open(0)
a,b,c=[0]*3
for i in r:
 T,C=i.strip().split()
 if T=="section":
  a+=1
  b,c=0,0
  print(f"{a}",C)
 elif T=="subsection":
  b+=1
  c=0
  print(f"{a}.{b}",C)
 else:
  c+=1
  print(f"{a}.{b}.{c}",C)