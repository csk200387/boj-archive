arr = list(map(int, input().split()))

d = {}
for i in range(len(arr)):
    data = input().split()
    for j in range(0, len(data), 2):
        if data[j] in d:
            d[data[j]]['sale'] += int(data[j+1])
            d[data[j]]['cnt'] += i
        else:
            d[data[j]] = {}
            d[data[j]]['sale'] = int(data[j+1])
            d[data[j]]['cnt'] = i

res = []
for key in d:
    if d[key]['sale'] >= 20 and d[key]['cnt'] == len(arr):
        res.append(key)

print(len(res), *res)