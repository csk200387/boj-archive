data = list(input())
stack = []
res = 0
tmp = 1
for i in range(len(data)):
    if data[i] == "(":
        stack.append(data[i])
        tmp *= 2
    elif data[i] == "[":
        stack.append(data[i])
        tmp *= 3
    elif data[i] == ")":
        if not stack or stack[-1] == "[":
            res = 0
            break
        if data[i-1] == "(":
            res += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == "(":
            res = 0
            break
        if data[i-1] == "[":
            res += tmp
        stack.pop()
        tmp //= 3
print(0 if stack else res)