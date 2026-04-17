n = int(input())
a, b = map(int, input().split())
if n == 1:
    print(0)
elif n == 2:
    print(2)
else:
    if a in [1, n] and b in [1, n]:
        print(2)
    elif a in [1, n] or b in [1, n]:
        print(3)
    else:
        print(4)