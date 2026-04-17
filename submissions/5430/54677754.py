import sys
from collections import deque

input = lambda:sys.stdin.readline().rstrip()
res = []
for _ in range(int(input())) :
    func = input()
    input()
    d = deque(eval(input()))
    status = False
    if func.count("D") > len(d) :
        print("error")
        # res.append("error")
    elif func.count("R") == len(func) :
        if func.count("R") % 2 == 0 :
            print(str(list(d)).replace(" ", ""))
        else :
            print(str(list(reversed(d))).replace(" ", ""))
    else :
        for t in func :
            if t == "R" :
                if status : # status가 True 일 때
                    status = False
                else :
                    status = True
            else :
                if status :
                    d.pop()
                else :
                    d.popleft()
        print(str(list(d)).replace(" ", ""))
        # res.append(str(list(d)))
# print(*res, sep="\n")
