import sys
input = sys.stdin.readline

n = int(input().rstrip())
for i in range(n) :
    t = int(input().rstrip())
    dic = {}
    for l in range(t) :
        tmp = input().rstrip().split()
        name, amount = tmp[0], int(tmp[1])
        dic[name] = amount
    print(max(dic, key=dic.get))