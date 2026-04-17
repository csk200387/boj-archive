y, m, d = map(int, input().split())
a, b, c = map(int, input().split())

A, B = y*365 + m*30 + d, a*365 + b*30 + c

r1, r2, r3 = None, a-y, a-y

if A < B:
    r2 += 1

if m == d and b == c:
    r1 = max(a-y, 0)
else:
    r1 = max(a-y-1, 0)

print(r1, r2, r3, sep="\n")