arr = list(map(int, open(0)))
mx = 0
for i in range(10):
    if mx == 100:
        break
    if mx <= 100:
        if (100-mx) == (mx+arr[i]-100):
            mx += arr[i]
            break
        elif mx+arr[i] > 100:
            break
        mx += arr[i]
print(mx)