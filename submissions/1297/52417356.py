import math
c, a, b = map(int, input().split())
t = a**2+b**2
res1 = math.floor((((c**2) / t)**0.5)*a)
res2 = math.floor((((c**2) / t)**0.5)*b)
print(res1, res2)