a,b=0,1;n=int(input())
for i in range(2,n):a,b=b,a+b
print(a+b if n != 0 else a)