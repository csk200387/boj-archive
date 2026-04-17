import sys
input = lambda:sys.stdin.readline().rstrip()
for _ in range(int(input())) :
    ar = []
    tmp = False
    for _ in range(int(input())) :
        ar.append(input())
    ar.sort()
    for i in ar :
        for l in range(ar.index(i)) :
            if ar[l].find(i) == 0 :
                tmp = True
                break
    if tmp :
        print("NO")
    else :
        print("YES")