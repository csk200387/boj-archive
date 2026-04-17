n = int(input())

a, b = map(int, input().split())

if n == 1:
    print(0)
elif n == 2:
    print(2)
else:
    if (a == 1 and b == 1) or (a == 1 and b == n) or (a == n and b == 1) or (a == n and b == n):
        print(2)
    elif a == 1 or b == 1 or a == n or b == n:
        print(3)
    else:
        print(4)