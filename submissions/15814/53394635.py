st = list(input())
for i in range(int(input())) :
    a, b = map(int, input().split())
    t = st[b]
    st[b] = st[a]
    st[a] = t
print(*st, sep="")