import sys
input = sys.stdin.readline
res = []
for p in range(9) :
    a = list(map(int,input().rstrip().split()))
    for l in a :
        res.append(l)
m = max(res)
e = res.index(m)+1
print(m)
print(((e-1)//9)+1,((e-1)%9)+1)