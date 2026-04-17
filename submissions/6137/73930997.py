import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
d = deque([input() for i in range(n)])
t = ""

while d:
    start, end = 0, len(d)-1
    pos = True
    while start <= end:
        if d[start] == d[end]:
            start += 1
            end -= 1
        elif d[start] < d[end]:
            pos = True
            break
        else:
            pos = False
            break
    if pos:
        t += d.popleft()
    else:
        t += d.pop()

print("\n".join([t[i:i+80] for i in range(0, len(t), 80)]))