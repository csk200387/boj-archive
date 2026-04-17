b, c = map(int, input().split())

x1 = int(-b - (b**2 - c)**.5)
x2 = int(-b + (b**2 - c)**.5)

if x1 == x2:
    print(x1)
else:
    print(x1, x2)