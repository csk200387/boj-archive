inf, *a = open(0)
_, name = inf.split()
chat, idx = "", 0
dic = {}
for i, t in enumerate(a):
    n, c = t.split()
    if name == n:
        idx = i
        chat = c
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1
print(sum(dic.values())-dic[c])