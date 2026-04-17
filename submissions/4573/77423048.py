c=1
while 1:
 n=int(input())
 if n==0:break
 else:
  print(f"Menu {c}:",min([tuple(map(int,input().split()))for i in range(n)],key=lambda x:x[1]/(3.14*(x[0]/2)**2))[0])
  c+=1