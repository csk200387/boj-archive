n, k = map(int, input().split())
pie = list(map(int, input().split()))
s = sum(pie[:k])
r = s
for i in range(k, k+n):
    ni = i%n
    s -= pie[ni-k]
    s += pie[ni]
    r = max(r,s)
print(r)