l,s=map(int,input().split())
d=input()
a,c,g,t=map(int,input().split())
A,C,G,T,r=0,0,0,0,0
for i in range(s):
 match d[i]:
  case'A':A+=1
  case'C':C+=1
  case'G':G+=1
  case'T':T+=1
if A>=a and C>=c and G>=g and T>=t:r+=1
for i in range(s,l):
 match d[i]:
  case'A':A+=1
  case'C':C+=1
  case'G':G+=1
  case'T':T+=1
 match d[i-s]:
  case'A':A+=1
  case'C':C+=1
  case'G':G+=1
  case'T':T+=1
 if A>=a and C>=c and G>=g and T>=t:r+=1
print(r)