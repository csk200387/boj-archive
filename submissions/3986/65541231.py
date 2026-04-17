import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
r = 0
for _ in range(n):
    data = list(input())
    stack = []
    for i in range(len(data)):
        tmp = data.pop()
        stack.append(tmp)
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
    if not stack:
        r += 1
print(r)