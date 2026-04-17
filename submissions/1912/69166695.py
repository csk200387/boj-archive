num = input()
arr = map(int, input().split())
res = 0
nxt = -10000
for n in arr:
    res = max(res+n, n)
    nxt = max(nxt, res)
print(nxt)