n,*r=open(0)
a,b,c=[0]*3
for i in r:
 T,C=i.strip().split()
 if T=="section":
  a,b,c=a+1,0,0
  print(f"{a}",C)
 elif T=="subsection":
  b,c=b+1,0
  print(f"{a}.{b}",C)
 else:
  c+=1
  print(f"{a}.{b}.{c}",C)