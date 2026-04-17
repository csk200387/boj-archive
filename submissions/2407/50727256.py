import math
from fractions import Fraction
a = list(map(int,input().split()))
fac = math.factorial(a[1])
res = 1
for i in range(a[1]):
    res *= a[0]-i
print(Fraction(res,fac))