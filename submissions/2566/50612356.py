res = []
for p in range(9) :
    a = list(map(int,input().split()))
    for l in a :
        res.append(l)
m = max(res)
e = res.index(m)+1
print(m)
print((e//9)+1,e%9)