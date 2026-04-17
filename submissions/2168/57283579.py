from math import gcd
x, y = map(int, input().split())
g = gcd(x,y)
print((x//g+y//g-1)*g)