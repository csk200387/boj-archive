size = int(input())
arr = list(map(int, input().split()))
r = 0
a = []
while arr:
    t = arr.pop()
    if t != 0:
        r += 1
    else:
        r = 0
    a.append(r)
print(max(a))