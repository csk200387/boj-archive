res = []
s = set(list(range(1,10001)))
for i in range(1,10001):
    a = sum(list(map(int,list(str(i))))) + i
    res.append(a)
for i in sorted(list(s-set(res))) :
    print(i)