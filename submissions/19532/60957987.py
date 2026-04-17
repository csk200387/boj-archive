a, b, c, d, e, f = map(int, input().split())
for x in range(0, 1000):
    for y in range(0, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)
            exit()
    for y in range(-1, -1000, -1):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)
            exit()
for x in range(-1, -1000, -1):
    for y in range(0, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)
            exit()
    for y in range(-1, -1000, -1):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)
            exit()