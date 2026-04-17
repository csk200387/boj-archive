from collections import deque

n = int(input())
arr = deque(enumerate(map(int, input().split())))
res = []

while arr:
    idx, val = arr.popleft()
    res.append(idx + 1)
    if val > 0:
        arr.rotate(-(val - 1))
    else:
        arr.rotate(-val)

print(*res)