import re
res = []
for i in range(int(input())) :
    r = re.findall(r"\d+", input())
    for i in r :
        num = int(i)
        res.append(num)
print(*sorted(res), sep="\n")