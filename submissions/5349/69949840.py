import sys
input = sys.stdin.readline
s = set()
result = set()
while True:
    t = input()
    if t == "000-00-0000\n":
        break
    if t in s:result.add(t)
    else:s.add(t)
print(*sorted(list(result), key=lambda x: (int(x.split("-")[0]), int(x.split("-")[1]), int(x.split("-")[2]))), sep="")