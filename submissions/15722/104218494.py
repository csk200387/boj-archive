n=int(input())
a=[(0,0)]
c=2
x,y=0,0
for i in range(35):
 c=i*2
 for t in range(c):
  if(c//2)%2==1:
   if t<c//2:y+=1
   else:x+=1
  else:
   if t<c//2:y-=1
   else:x-=1
  a.append((x,y))
print(*a[n])