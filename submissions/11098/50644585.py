n = int(input())
for i in range(n) :
    num = int(input())
    res = []
    for l in range(num) :
        a = input().split()
        res.append(a)
    res.sort(key = lambda x:x[0], reverse=True)
    print(res[0][1])