res = []
for _ in range(5) :
    res.append(sum(map(int, input().split())))
print(res.index(max(res))+1, max(res))