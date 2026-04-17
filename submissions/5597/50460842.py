a = set(list(range(1,31)))
b = []
for i in range(28):
    t = int(input())
    b.append(t)
a = sorted(list(a-set(b)))
print(a[0])
print(a[1])