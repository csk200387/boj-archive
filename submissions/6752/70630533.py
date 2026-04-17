n, *arr = map(int, open(0))

arr.sort()
s, i = 0, 0
while s <= n:
    s += arr[i]
    if s > n:
        s -= arr[i]
        break
    i += 1

print(i)