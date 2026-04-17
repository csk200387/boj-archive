from collections import Counter
C=Counter(input())
C=sorted(C.items(), key=lambda x: x[0])
t=0
for i in C:
 if i[1]%2!=0:
  t+=1
  if t>1:
   print("I'm Sorry Hansoo")
   exit(0)
s,t="",""
for x,y in C:
 if y%2!=0:t=x
 s+=x*(y//2)
print(s+t+s[::-1])