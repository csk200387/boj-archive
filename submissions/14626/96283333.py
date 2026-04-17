n = input()
r = 0
hs = 0
for i in range(12):
    if n[i] == "*":
        hs = 1 if i%2==0 else 3
    else:
        if i%2 == 0:
            r += int(n[i])
        else:
            r += 3*int(n[i])
for i in range(1, 10):
    t = r+i*hs
    if 10-t%10 == int(n[-1]):
        print(i)
        exit(0)
print(0)