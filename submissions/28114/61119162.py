arr = [*open(0)]

arr.sort(key=lambda x: int(x.split()[1]))
for i in arr:
    t = i.split()[1][2:]
    print(t, end="")
print()
arr.sort(key=lambda x: int(x.split()[0]), reverse=True)
for i in arr:
    t = i.split()[2][0]
    print(t, end="")
print()