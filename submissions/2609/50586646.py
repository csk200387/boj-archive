import math
def lcm(x, y):
    return (x * y) // math.gcd(x, y)
a = input().split()
print(math.gcd(int(a[0]),int(a[1])))
print(lcm(int(a[0]),int(a[1])))