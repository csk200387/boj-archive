a, b = map(int,input().split())
ar = []
for _ in range(2) :
    ar.append(list(map(int,input().split())))
re = ar[0]+ar[1]
print(*sorted(re), sep=" ")