for i in open(0):
 L,l=i.strip(),set()
 for x in range(len(L)):
  for y in range(x,len(L)):
   if (t:=L[x:y+1]) == t[::-1]:l.add(t)
 r='" "'.join(sorted([*l],key=lambda x:(len(x),L.index(x))))
 print(f'{len(l)} - "{r}"')