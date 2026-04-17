d = input()
c = d.count('a')
d += d[:c-1]
mn = 1000
for i in range(len(d)-c+1):
    t = d[i:i+c].count('b')
    if mn > t:
        mn = t
print(mn)