n = int(input())
cnt = 0
s = 0
start, end = 0, 0

while end <= n:
    if s < n:
        end += 1
        s += end
    elif s > n:
        s -= start
        start += 1
    else:
        cnt += 1
        end += 1
        s += end

print(cnt)