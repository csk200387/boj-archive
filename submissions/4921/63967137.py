import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

TRY = 0
while True:
    TRY += 1
    data = input()
    
    if data == "0": # 종료 값 입력
        break

    if data[0] != "1" or data[-1] != "2": # 시작이 1, 끝이 2가 아닌 경우
        print(f"{TRY}. NOT")
        continue
    if len(data) % 2 == 0:
        print(f"{TRY}. NOT")
        continue

    # START
    data = deque(map(int, list(data)))
    stack = [data.popleft()]
    t = True
    while data:
        tmp = data.popleft()
        pre = stack[-1]
        if pre in [1, 3] and tmp in [4, 5]:
            stack.append(tmp)
        elif pre in [4, 6] and tmp in [2, 3]:
            stack.append(tmp)
        elif pre in [5, 7] and tmp == 8:
            stack.append(tmp)
        elif pre == 8 and tmp in [6, 7]:
            stack.append(tmp)
        else:
            print(f"{TRY}. NOT")
            t = False
            break
    if t:
        print(f"{TRY}. VALID")