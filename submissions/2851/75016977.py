arr = list(map(int, open(0)))
mx = 0
for i in range(10):
    mx += arr[i]
    if mx >= 100:
        if mx - 100 > 100 - mx+arr[i]:
            mx -= arr[i]
        break
print(mx)