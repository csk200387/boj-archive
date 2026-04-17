a = []
for i in range(1,10001) :
    if i**2 >= 10001 :
        break
    else :
        a.append(i**2)
n = int(input())
m = int(input())
res = []
for i in a :
    if i >= n and i <= m :
        res.append(i)
if len(res) == 0 :
    print(-1)
else :
    print(sum(res))
    print(min(res))