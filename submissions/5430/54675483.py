import sys
from collections import deque

input = lambda:sys.stdin.readline().rstrip()
res = []
for _ in range(int(input())) :
    func = input()
    input()
    d = deque(eval(input()))
    if func.count("D") >= len(d) :
        print("error")
    else :
        for t in func :
            if t == "R" :
                d.reverse()
            else :
                d.popleft()
        print(list(d))