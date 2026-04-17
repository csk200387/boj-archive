n = int(input())
d=input()
r=0
for c in d:
 if c=='N':r+=1
 if c=='S':r-=1
 if c=='E':r+=1
 if c=='W':r-=1
print(abs(r))