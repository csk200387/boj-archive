n, k = map(int, input().split())
pie = list(map(int, input().split()))
pie += [pie[0]]
s = sum(pie[:k])
for i in range(k, n):
    t = s - pie[i-k] + pie[i]
    if s < t:
        s = t
print(s)