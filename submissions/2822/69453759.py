d = {int(input()):i+1 for i in range(8)}
for i in sorted(d.keys())[:3]:del d[i]
print(sum(d.keys()))
print(*sorted(d.values()))