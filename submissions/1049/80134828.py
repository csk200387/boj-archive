import sys
input = lambda:sys.stdin.readline().rstrip()

n, m = map(int,input().split())

a = []
b = []

for _ in range(m):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

s = min(a)
o = min(b)

if s < o * 6:
    if s < (n % 6) * o:
        print((n // 6) * s + s)
    else:
        print((n // 6) * s + (n % 6) * o)

elif s >= o * 6:
    print(n * o)