aa = input()
inp = list(map(int,input().split()))
res = []
for a in inp :
    e = 0
    for i in range(2,a+1):
        if a % i == 0 :
            e += 1
        if i == a and e == 1:
            res.append(a)
print(len(res))