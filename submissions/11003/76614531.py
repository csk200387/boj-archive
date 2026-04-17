from collections import deque
n, l = map(int, input().split())
arr = deque(list(map(int, input().split())))
res = []
deq = deque()
for i in range(n):
    if i < l:
        deq.append(arr.popleft())
        res.append(min(deq))
    else:
        deq.append(arr.popleft())
        deq.popleft()
        res.append(min(deq))
print(" ".join(map(str,res)))