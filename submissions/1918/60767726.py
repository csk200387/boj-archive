stack = []
s = input()
i = 0
while len(s) > i:
    I = s[i]
    if I.isalpha():
        print(I, end="")
    else:
        if I == "(":
            stack += [I]
        elif I == "*" or I == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                print(stack.pop(), end="")
            stack += [I]
        elif I == "+" or I == "-":
            while stack and stack[-1] != "(":
                print(stack.pop(), end="")
            stack += [I]
        elif I == ")":
            while stack and stack[-1] != "(":
                print(stack.pop(), end="")
            stack.pop()
    i += 1
while stack:
    print(stack.pop(), end="")