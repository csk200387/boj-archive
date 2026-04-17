import sys
from collections import deque

input = lambda:sys.stdin.readline().rstrip()

for _ in range(int(input())) :
    func = input()
    input()
    d = deque(eval(input()))
    isError = False
    status = False

    for t in func :
        if t == "R" :
            if status : # status가 True 일 때
                status = False
            else :
                status = True
        else :
            if len(d) < 1 :
                isError = True
                break
            else :
                if status :
                    d.pop()
                else :
                    d.popleft()
    if isError :
        print("error")
    else :
        if func.count("R") % 2 == 0 :
            print(str(list(d)).replace(" ", ""))
        else :
            print(str(list(reversed(d))).replace(" ", ""))