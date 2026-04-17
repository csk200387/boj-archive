N, M = map(int, input().split())
res = []
for i in range(1,N+1) :
    if N % i == 0 :
        res.append(i)
try :
    print(res[M-1])
except IndexError :
    print(0)