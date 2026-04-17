n, k = map(int, input().split())
pie = list(map(int, input().split()))
s = sum(pie[:k])
for i in range(k, k+n):
    ni = i%n
    t = s - pie[ni-k] + pie[ni]
    if s < t:
        s = t
print(s)