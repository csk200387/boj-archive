ct = 0
n = int(input())
while n > 0:
    if n % 5 == 0:
        ct += n // 5
        break
    n -= 2
    ct += 1
if n < 0:
    print(-1)
else:
    print(ct)