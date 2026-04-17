aa = int(input())
inp = int(input())
res = []
for a in range(aa,inp+1) :
    e = 0
    for i in range(2,a+1):
        if a % i == 0 :
            e += 1
        if i == a and e == 1:
            res.append(a)
if len(res) == 0 :
    print(-1)
else :
    print(sum(res))
    print(res[0])