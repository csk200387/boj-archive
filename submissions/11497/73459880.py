import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()
for _ in range(int(input())):
    input()
    arr = sorted(map(int, input().split()))
    d = deque()
    for i in range(len(arr)):
        if i % 2 == 0:
           d.appendleft(arr.pop())
        else:
            d.append(arr.pop())
    mn = abs(d[0]-d[1])
    for i in range(2, len(d)):
        if mn < abs(d[i-1]-d[i]):
            mn = abs(d[i-1]-d[i])
    print(mn)