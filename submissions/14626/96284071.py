n = input().strip()
r = 0
hs = 0
m = int(n[-1])
for i in range(12):
    if n[i] == "*":
        hs = 1 if i%2==0 else 3
    else:
        if i%2 == 0:
            r += int(n[i])
        else:
            r += 3*int(n[i])
for i in range(10):
    if (m+r+i*hs)%10 == 0:
        print(i)
        break