import time
ar = []
for _ in range(int(input())) :
    ar.append(int(input()))
print(*sorted(ar),sep="\n")