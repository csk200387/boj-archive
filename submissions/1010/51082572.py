import math
fac = lambda x:math.factorial(x)
for i in range(int(input())) :
    r, n = map(int, input().split())
    print(int(fac(n)/(fac(r)*fac(n-r))))