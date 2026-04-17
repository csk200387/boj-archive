from collections import Counter

string = input()
count = Counter(string)
tmp = 0
for i in count.values():
    if i % 2 != 0:
        tmp += 1
if tmp > 1:
    print("I'm Sorry Hansoo")
    exit(0)

st, t = "", ""
if len(string) % 2 == 0:
    for x, y in zip(count.keys(), count.values()):
        st += x * (y // 2)
else :
    for x, y in zip(count.keys(), count.values()):
        if y % 2 != 0:
            t = x
        st += x * (y // 2)
print(st + t + st[::-1])