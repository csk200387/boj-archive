from collections import Counter
C=Counter(input())
C=sorted(C.items(), key=lambda x: x[0])
t=0
for i in C:
 if i[1]%2!=0:
  t+=1
  if t>1:
   exit(print("I'm Sorry Hansoo"))
s=""
for x,y in C:
 if y%2!=0:s+=x
 s+=x*(y//2)
print(s[:-1]+s[::-1])