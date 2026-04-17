import sys
while True:
 try:
  m=[int(sys.stdin.readline(),2)for _ in range(32)]
  a=0
  p=0
  while True:
   c=m[p]//2**5
   v=m[p]%2**5
   p+=1
   p%=32
   match c:
    case 0:m[v]=a
    case 1:a=m[v]
    case 2:
     if not a:p=v
    case 3:pass
    case 4:a=(a+255)%2**8
    case 5:a=(a+1)%2**8
    case 6:p =v
    case 7:break
  print(f"{a:08b}")
 except:break