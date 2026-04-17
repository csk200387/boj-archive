import sys
input = lambda:sys.stdin.readline().rstrip()
for _ in range(int(input())) :
    ar = ["@"]
    tmp = False
    for _ in range(int(input())) :
        t = input()
        for i in ar :
            if t.find(i) == 0 :
                tmp = True
                break
        ar.append(t)
    if tmp :
        print("NO")
    else :
        print("YES")