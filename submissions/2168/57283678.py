import math
x,y=map(int,input().split())
g=math.gcd(x,y)
print((x//g+y//g-1)*g)