import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

_try = int(input())

for _ in range(_try):
    N, M = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    cnt = 0
    
    while queue:
        max_val = max(queue)
        val = queue.popleft()
        M -= 1

        if val == max_val:
            cnt += 1
            if M < 0:
                print(cnt)
                break
        else:
            queue.append(val)
            if M < 0:
                M = len(queue) - 1