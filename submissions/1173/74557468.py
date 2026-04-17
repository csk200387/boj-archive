N, m, M, T, R = map(int, input().split())
start, prev, cnt, exc = m, 0, 0, 0
while exc != N:
    prev = start
    if start+T <= M:
        start += T
        exc += 1
    else:
        start -= R
        if start <= m:
            start = m
    if prev == start:
        break
    cnt += 1
print(cnt if cnt else -1)