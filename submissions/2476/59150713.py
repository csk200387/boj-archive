res = []
for i in range(int(input())):
    d1, d2, d3 = map(int,input().split())
    if d1 == d2 == d3 :
        res.append(10000 + d1 * 1000)
    elif d1 == d2 or d3 == d1 :
        res.append(1000 + d1 * 100)
    elif d2 == d3 :
        res.append(1000 + d2 * 100)
    else :
        if d1 > d2 and d1 > d3 :
            res.append(d1*100)
        elif d2 > d1 and d2 > d3 :
            res.append(d2*100)
        else :
            res.append(d3*100)
print(max(res))