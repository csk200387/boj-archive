stack = []
for line in [*open(0)][1::]:
    i = [*map(int, line.split())]

    if i[0] == 1:
        stack.append(i[1])
    elif i[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif i[0] == 3:
        print(len(stack))
    elif i[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)