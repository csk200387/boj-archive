s = input()
for i in range(len(s), 0, -1):
    t = s+s[::-1][i:]
    if t == t[::-1]:
        print(len(t))
        break