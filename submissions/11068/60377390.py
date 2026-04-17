def jinsu(a,b):
    r = []
    while a > 0:
        r.append(a%b)
        a = a//b
    r = r[::-1]
    return r

for i in range(int(input())) :
    n = int(input())
    b = False
    for i in range(2,65):
        if jinsu(n,i) == jinsu(n,i)[::-1]:
            b = True
            break
    if b:
        print(1)
    else:
        print(0)