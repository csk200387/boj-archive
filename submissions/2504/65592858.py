data = input()

stack = []
result = 0

try:
    for i in range(len(data)):
        if data[i] == '(' or data[i] == '[':
            stack.append(data[i])
        elif data[i] == ')':
            if data[i-1] == '(':
                stack.pop()
                stack.append(2)
            else:
                temp = 0
                while stack:
                    top = stack.pop()
                    if top == '(':
                        stack.append(temp*2)
                        break
                    elif top == '[':
                        print(0)
                        exit(0)
                    else:
                        temp += top
        elif data[i] == ']':
            if data[i-1] == '[':
                stack.pop()
                stack.append(3)
            else:
                temp = 0
                while stack:
                    top = stack.pop()
                    if top == '[':
                        stack.append(temp*3)
                        break
                    elif top == '(':
                        print(0)
                        exit(0)
                    else:
                        temp += top
        else:
            print(0)
            exit(0)

    for i in stack:
        if i == '(' or i == '[':
            print(0)
            exit(0)
        else:
            result += i

    print(result)
except:
    print(0)