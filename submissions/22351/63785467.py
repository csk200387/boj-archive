# 백준 테스트
from collections import deque

s = input()
deq = deque(s)
right = ""
left = ""
try:
    while True:
        right += deq.popleft()
        left += deq.pop()
        r = int(right)
        l = int(left)
        t = "".join([str(i) for i in range(r,l+1)])
        if s == t:
            print(r, l)
            break
        
        if r > l:
            left += deq.popleft()
        elif l < r:
            right += deq.pop()
        elif l == r:
            left += deq.popleft()
        else:
            right += deq.pop()
except IndexError:
    print(s, s)