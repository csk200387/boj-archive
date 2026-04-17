d,a=26,input()
for i in range(d):
 if a.count(chr(97+i))>0:
  d-=1
print(d if d!=0 else "impossible")