input()
a = list(map(int, input().split()))
s1, s2 = 0, 0
for i in a:
    s1 += i
    s2 += i // 2
if sum(a) % 3 != 0:
    print("NO")
else:
    if s2 >= s1//3:
        print("YES")
    else:
        print("NO")