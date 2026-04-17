a, b, c = map(int, input().split())
a -= 2*c
b -= 2*c
if a <= 0 or b <= 0:
    print(0)
else:
    print(a*b)