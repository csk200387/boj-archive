from collections import Counter

string = input()
count = Counter(string)
count = sorted(count.items(), key=lambda x: x[0])
tmp = 0
for i in count:
    if i[1] % 2 != 0:
        tmp += 1
if tmp > 1:
    print("I'm Sorry Hansoo")
    exit(0)

st, t = "", ""
if len(string) % 2 == 0:
    for x, y in count:
        st += x * (y // 2)
else :
    for x, y in count:
        if y % 2 != 0:
            t = x
        st += x * (y // 2)
print(st + t + st[::-1])