from collections import Counter
c = Counter()
while True:
    line = input()
    if line == "***":
        break
    c[line] += 1
w = max(c.values())
print('Runoff!' if list(c.values()).count(w)>1 else [k for k,v in c.items() if v==w][0])