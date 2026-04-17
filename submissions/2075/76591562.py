from heapq import *
import sys
hq = []
n = int(input())
for i in range(n):
    t = list(map(int, sys.stdin.readline().split()))
    for c in t:
        if i == 0:
            heappush(hq, c)
        else:
            heappushpop(hq, c)
print(heappop(hq))