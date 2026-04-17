num = int(input())
for i in range(num) :
    a = input().split()
    res = []
    for l in a :
        res.append(l[::-1])
    print(" ".join(res))