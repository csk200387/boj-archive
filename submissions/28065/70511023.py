from collections import deque

arr = deque(range(1, int(input())+1))

res = []
res.append(arr.popleft())

i = 0
while arr:
    if i % 2 == 0:
        res.append(arr.pop())
    else:
        res.append(arr.popleft())
    i += 1

print(*res)