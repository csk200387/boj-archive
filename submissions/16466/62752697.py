input()
s = sorted(map(int, input().split()))
t = 1
for i in s:
    if i != t:
        print(t)
        break
    t += 1