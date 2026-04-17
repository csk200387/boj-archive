n = int(input())

a, b = map(int, input().split())

if n == 1:
    print(0)
elif n == 1:
    print(2)
else:
    if a == 1 and b == 1:
        print(2)
    elif a == 1 or b == 1:
        print(3)
    else:
        print(4)