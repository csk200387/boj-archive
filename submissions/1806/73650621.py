n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
mn = []
sm = 0
start, end = 0, 0
while True:
    try:
        if sm < s:
            sm += arr[end]
            end += 1
        elif sm >= s:
            mn.append(end - start)
            sm -= arr[start]
            start += 1
    except IndexError:
        break
print(min(mn)if mn else 0)