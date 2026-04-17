a, b = map(int, input().split())
if not a % 2 == 0 and not b % 2 == 0:
    print(min(a, b))
else:
    print(0)