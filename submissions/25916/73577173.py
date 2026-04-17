n, m = map(int, input().split())
arr = list(map(int, input().split()))
mx = []
start, end = 0, 0
sm = 0

while True:
    try:
        if sm <= m:
            sm += arr[end]
            mx.append(sm if sm <= m else 0)
            end += 1
        else:
            sm -= arr[start]
            start += 1
    except IndexError:
        break

print(max(mx))