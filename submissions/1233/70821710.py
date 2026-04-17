from collections import defaultdict
a, b, c = map(int, input().split())
d = defaultdict(int)
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            d[i+j+k] += 1
print(max(d, key=d.get))