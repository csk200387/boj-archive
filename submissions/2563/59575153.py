arr = [[0]*100 for _ in range(100)]
for i in range(int(input())) :
    x, y = map(int, input().split())
    for a in range(x, x+10) :
        for b in range(y, y+10) :
            arr[b][a] = 1
print(sum([t.count(1) for t in arr]))