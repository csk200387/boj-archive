import sys
input = lambda:sys.stdin.readline().rstrip()
for _ in range(int(input())) :
    ar = ["@"]
    tmp = False
    for _ in range(int(input())) :
        t = input()
        #print(ar)
        for i in ar :
            if t.find(i) == 0 :
                tmp = True
        ar.append(t)
    if tmp :
        print("NO")
    else :
        print("YES")