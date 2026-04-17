d = {'@': 'a', '[': 'c', '!': 'i', ';': 'j', '^': 'n', '0': 'o',
     '7': 't', "\\\\'": 'w', "\\'": 'v'}

for _ in range(int(input())):
    inp = input()
    ct = 0
    stack = []
    for i in inp:
        if i in d.keys():
            stack.append(d[i])
            ct += 1
        else:
            stack.append(i)
        if stack[-3:] == list("\\\\'"):
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append("w")
            ct += 1
        if stack[-2:] == list("\\'"):
            stack.pop()
            stack.pop()
            stack.append("v")
            ct += 1
    inp = "".join(stack)
    print(inp if ct*2 < len(inp) else "I don't understand")