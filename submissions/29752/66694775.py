size = int(input())
arr = list(map(int, input().split()))
r = 0
a = []
while arr:
    t = arr.pop()
    if t != 0:
        r += 1
        a.append(r)
    else:
        r = 0
print(max(a))