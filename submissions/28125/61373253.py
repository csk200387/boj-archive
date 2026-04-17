s = ['a', 'c', 'i', 'j', 'n', 'o', 't', 'v', 'w']
t = ['@', '[', '!', ';', '^', '0', '7', "\\'", "\\\\'"]

for _ in range(int(input())):
    inp = input()
    ct = 0
    for i in t:
        if i in inp:
            ct += 1
        inp = inp.replace(i, s[t.index(i)])
    print(inp if ct < len(inp)//2 else "I don't understand")