x,y=map(int,input().split())
mx=0
for i in range(2,y+1):
 if(n:=int(str(i*x)[::-1]))>mx:mx=n
print(mx)