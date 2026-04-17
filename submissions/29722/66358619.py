y, m, d = map(int, input().split("-"))
cycle = int(input())

d += cycle
if d > 30:
    m += d // 30
    d = d % 30

if m > 12:
    y += m // 12
    m = m % 12

if m == 0:
    m = 12
    y -= 1

if d == 0:
    d = 30
    m -= 1


print("%d-%02d-%02d" % (y, m, d))