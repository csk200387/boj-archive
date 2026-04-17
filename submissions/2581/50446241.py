aa = int(input())
inp = int(input())
res = []
for a in range(aa,inp+1) :
    e = True
    for i in range(2,a+1):
        if a % i == 0 :
            e = False
            break
        if e == False:
            res.append(i)
print(res)