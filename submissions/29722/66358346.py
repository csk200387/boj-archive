y, m, d = map(int, input().split("-"))
cycle = int(input())

d += cycle
if d > 30:
    m += d // 30
    d = d % 30
if m > 12:
    y += m // 12
    m = m % 12

print("%d-%02d-%02d" % (y, m, d))