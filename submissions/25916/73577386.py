n, m = map(int, input().split())
arr = list(map(int, input().split()))
mx = 0
start, end = 0, 0
sm = 0

while True:
    try:
        if sm <= m:
            if sm > mx:
                mx = sm
            sm += arr[end]
            end += 1
        else:
            sm -= arr[start]
            start += 1
    except IndexError:
        break

print(mx)