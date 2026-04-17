import math
for _ in range(5) :
    a, b = map(int, input().split())
    print(math.gcd(math.factorial(a), b))