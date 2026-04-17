l, r, n = map(int, [i.strip() for i in open(0)])
count = 0
for i in range(l, r+1):
    for j in range(i+1, r+1):
        if (j - i) % n == 0:
            count += 1
print(count)