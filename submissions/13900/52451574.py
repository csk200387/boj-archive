from itertools import combinations
input()
a = list(map(int, input().split()))
res = 0
for i in combinations(a,2) :
    res += i[0]*i[1]
print(res)