n = int(input())
arr = list(range(1, n+1))
cnt = 0
s = 0
start, end = 0, 0

while True:
    try:
        if s >= n:
            if s == n:
                cnt += 1
            s -= arr[start]
            start += 1
        else:
            s += arr[end]
            end += 1
    except IndexError:
        break
print(cnt)