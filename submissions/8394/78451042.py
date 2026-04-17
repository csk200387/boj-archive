a,b=0,1
for i in range(int(input())):
  a,b=b%10,(a+b)%10
print(b)