import math
num = int(input())
for i in range(num) :
    a = list(map(int,input().split()))
    gcd = math.gcd(a[0], a[1])
    lcm = (a[0] * a[1]) // gcd
    print(lcm,gcd)