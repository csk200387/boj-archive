d = input()
r = 0
for i in range(len(d)):
    r += int(d[i:]+d[:i])
print(r)