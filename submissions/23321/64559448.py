a = [list(i.strip()) for i in open(0)]
l = len(a[0])
for i in range(l):
    if a[0][i] == '.' and a[1][i] == 'o':
        for x,y in zip(range(5), 'owln.'):
            a[x][i] = y
    elif a[0][i] == 'o':
        for x,y in zip(range(5), '.omln'):
            a[x][i] = y
for i in a:
    print(''.join(i))