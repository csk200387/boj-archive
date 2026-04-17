import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
stack = {i for i in range(n)}
for i in range(1, n, 2):
    stack.remove(i)
for i in range(0, n, 2):
    if len(stack) == 1:
        print(stack.pop()+1)
        break
    stack.remove(i)