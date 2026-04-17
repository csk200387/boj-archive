inf, *a = open(0)
_, name = inf.split()
for i, t in enumerate(a):
    n, c = t.split()
    if name == n:
        print(i)
        break