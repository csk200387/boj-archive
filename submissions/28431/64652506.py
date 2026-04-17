t = set()
for i in open(0):
    if i in t:t.remove(i)
    else:t.add(i)
print(*t, end='')