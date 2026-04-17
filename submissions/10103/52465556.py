res = [100,100]
for i in range(int(input())) :
    a, b = map(int,input().split())
    if a > b :
        res[1] -= a
    elif a < b :
        res[0] -= b
print(*res, sep="\n")