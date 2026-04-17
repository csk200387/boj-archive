n,m = map(int, input().split())
for i in range(n) :
    tmp = []
    for l in range(1,m+1) :
        tmp.append((i*m)+l)
    print(" ".join(list(map(str,tmp))))