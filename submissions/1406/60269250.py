import sys
input = lambda:sys.stdin.readline().rstrip()

rStack = [input()]
lStack = []

for _ in range(int(input())):
    cmd = input()
    if cmd == 'L':
        if rStack:
            lStack.append(rStack.pop())
    elif cmd == 'D':
        if lStack:
            rStack.append(lStack.pop())
    elif cmd == 'B':
        if rStack:
            rStack.pop()
    else:
        rStack.append(cmd[2])

print(''.join(rStack + lStack[::-1]))