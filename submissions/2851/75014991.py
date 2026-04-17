arr = list(map(int, open(0)))
mx = 0
for i in range(10):
    tmp = mx + arr[i]
    if tmp <= 100:
        mx = tmp
    if tmp >= 100:
        if abs(100-mx) == abs(100-tmp):
            print(tmp)
        else:
            print(mx)
        exit()
print(mx)