for i in range(int(input())):
 d=input()
 p=1
 C=1
 for j in range(len(d)//2):
  if d[j]!=d[-1-j]:
   p=0
   break
  C+=1
 print(int(p), C)