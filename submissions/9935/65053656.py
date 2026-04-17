import sys
input = lambda:sys.stdin.readline().rstrip()
data = input()
tg = list(input())
stack = []
for i in range(len(data)):
    stack += data[i]
    if len(stack) >= len(tg):
        if stack[-len(tg):] == tg:
            del stack[-len(tg):]
if stack:
    print(''.join(stack))
else:
    print('FRULA')