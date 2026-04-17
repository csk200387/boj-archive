from math import gcd
a,b = map(int, input().split())
c,d = map(int, input().split())
res1 = a*d + c*b
res2 = d*b
cd = gcd(res1, res2)
print(res1//cd, res2//cd)