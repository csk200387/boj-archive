arr = list(map(int, input().split()))

di = {}
for i in range(len(arr)):
    data = input().split()
    d = {}
    for j in range(0, len(data), 2):
        if data[j] in d:
            d[data[j]]['sale'] += int(data[j+1])
        else:
            d[data[j]] = {}
            d[data[j]]['sale'] = int(data[j+1])
            d[data[j]]['cnt'] = i
    for key in d:
        if d[key]['sale'] >= 20:
            if key in di:
                di[key] += 1
            else:
                di[key] = 1

print(di)
res = []
for key in di:
    print(key)
    if di[key] == len(arr):
        res.append(key)

print(len(res), *res)