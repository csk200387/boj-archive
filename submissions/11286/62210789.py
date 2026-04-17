import heapq as h
import sys
input = lambda:sys.stdin.readline().rstrip()
ar = []
for _ in range(int(input())) :
    t = int(input())
    if t == 0 :
        if len(ar) == 0 :
            print(0)
        else :
            a,b = h.heappop(ar)
            print(a*b)
    else :
        h.heappush(ar, (abs(t), 1 if t > 0 else -1))