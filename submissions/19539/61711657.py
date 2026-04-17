input()
a = tuple(map(int, input().split()))
s1, s2 = 0, 0
for i in a:
    s1 += i
    s2 += i // 2
if sum(a) % 3 != 0:
    print("NO")
else:
    print("YES" if s2 >= s1//3 else "NO")