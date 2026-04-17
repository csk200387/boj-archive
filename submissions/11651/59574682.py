n, *ar = open(0)
ar = [[*map(int, i.split())] for i in ar]
ar.sort(key=lambda x:(x[1], x[0]))
for x in ar :
    print(*x)