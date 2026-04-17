from collections import Counter
inp = input()
c = list(dict(Counter(inp)).values())
stack = 0
for i in c :
    if i%2 == 0 :
        stack += 1
    else :
        pass
if stack == len(c) :
    print(0)
elif stack == 0 :
    print(1)
else :
    print("0/1")