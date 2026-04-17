import sys
input = lambda:sys.stdin.readline().rstrip()
r = []
for i in range(int(input())) :
    t = list(map(int, input().split()))
    tmp = 0
    for l in range(10) :
        if t[l] == (l%5)+1 :
            tmp += 1
    if tmp == 10 :
        r.append(i+1)
print(*r, sep="\n")