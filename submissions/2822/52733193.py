d = {}
for i in range(1,9) :
    d[int(input())] = i
for i in sorted(d.keys())[:3] :
    del d[i]
print(sum(d.keys()))
print(*sorted(d.values()))