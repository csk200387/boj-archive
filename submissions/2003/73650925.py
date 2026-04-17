n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
s = 0
start, end = 0, 0

while True:
    try:
        if s >= m:
            if s == m:
                cnt += 1
            s -= arr[start]
            start += 1
        else:
            s += arr[end]
            end += 1
    except IndexError:
        break

print(cnt)