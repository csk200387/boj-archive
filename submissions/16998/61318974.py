import sys
input = lambda:sys.stdin.readline().rstrip()

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

for _ in range(int(input())) :
    p, q, n = map(int, input().split())
    s = 0
    g = gcd(p, q)
    p = p // g
    for i in range(1, n+1) :
        s += (p % q) * (i % q) % q
    print(s)