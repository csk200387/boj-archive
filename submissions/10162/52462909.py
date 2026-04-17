n = int(input())
a = n//300
n -= 300*a
b = n//60
n -= 60*b
c = n//10
if n%10 == 0 :
    print(a,b,c)
else :
    print(-1)