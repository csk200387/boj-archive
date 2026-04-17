n = int(input())
r = 0
for i in range(0, n + 1):
    for l in range(i, n + 1):
        r += i + l
print(r)