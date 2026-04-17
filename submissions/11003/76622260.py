from collections import deque
n, l = map(int, input().split())
arr = list(map(int, input().split()))
deq = deque()
for i in range(n):
    t = arr[i]
    while deq and deq[-1][0] > t:
        deq.pop()
    while deq and deq[0][1] < i-l+1:
        deq.popleft()
    deq.append((t,i))
    print(deq[0][0], end=" ")