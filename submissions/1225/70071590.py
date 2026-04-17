def calc(s, l):
    sums = sum(map(int, list(l)))
    res = 0
    for i in s:
        res += sums*int(i)
    return res
a, b = input().split()
if len(a) < len(b):t = calc(a,b)
else:t = calc(b,a)
print(t)