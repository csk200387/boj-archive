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
        if stack[-2:] == list("\\'"):
            stack.pop()
            stack.pop()
            stack.append("v")
            ct += 1
        if stack[-3:] == list("\\\\'"):
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append("w")
            ct += 1
    inp = "".join(stack)
    print(inp if ct <= len(inp)//2 else "I don't understand")
    # for i in t:
    #     if i in inp:
    #         ct += 1
    #     inp = inp.replace(i, s[t.index(i)], 1)
    # print(inp if ct <= len(inp)//2 else "I don't understand")