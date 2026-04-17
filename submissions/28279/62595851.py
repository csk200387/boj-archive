from collections import deque
import sys
input = lambda:sys.stdin.readline()

d = deque()

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == "1":
        d.appendleft(int(cmd[1]))
    elif cmd[0] == "2":
        d.append(int(cmd[1]))
    elif cmd[0] == "3":
        print(d.popleft() if d else -1)
    elif cmd[0] == "4":
        print(d.pop() if d else -1)
    elif cmd[0] == "5":
        print(len(d))
    elif cmd[0] == "6":
        print(0 if d else 1)
    elif cmd[0] == "7":
        print(d[0] if d else -1)
    else:
        print(d[-1] if d else -1)