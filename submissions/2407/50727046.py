import math
a = list(map(int,input().split()))
fac = math.factorial(a[1])
res = 1
for i in range(a[1]):
    res *= 100-i
print(int(res/fac))