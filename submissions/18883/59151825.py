n,m = map(int, input().split())
for i in range(n) :
    tmp = [(i*m)+l for l in range(1, m+1)]
    print(*tmp)