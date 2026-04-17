n = int(input())
for i in range(n) :
    t = int(input())
    dic = {}
    for l in range(t) :
        name, amount = input().split()
        dic[name] = int(amount)
    print(max(dic, key=dic.get))