import sys
input = lambda:sys.stdin.readline().rstrip()
ar = []
for _ in range(int(input())) :
    ar.append(int(input()))
print(*sorted(ar),sep="\n")