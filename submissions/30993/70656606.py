import math
fac = lambda x:math.factorial(x)
n, a, b, c = map(int, input().split())
print(fac(n) // (fac(a) * fac(b) * fac(c)))