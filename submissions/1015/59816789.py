a,b=open(0)
a = [*map(int, b.split())]
t = sorted(a, reverse=0)
for i in range(len(t)) :
    p = t.index(a[i])
    print(p, end=" ")
    t[p] = -1