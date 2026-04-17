import time
ar = []
for _ in range(int(input())) :
    ar.append(list(map(int, input().split())))
ar.sort(key=lambda x:(x[1], x[0]))
for x, y in ar :
    print(x,y)