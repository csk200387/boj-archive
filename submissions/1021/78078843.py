from collections import deque
n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
deq = deque(range(1, n+1))
for i in arr:
    if deq[0] == i:
        deq.popleft()
    else:
        if len(deq)/2 > deq.index(i):
            while deq[0] != i:
                deq.append(deq.popleft())
                cnt += 1
        else:
            while deq[0] != i:
                deq.appendleft(deq.pop())
                cnt += 1
        deq.popleft()
print(cnt)