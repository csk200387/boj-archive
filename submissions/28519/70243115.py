a, b = map(int, input().split())
if abs(a-b) == 1 or a-b == 0:
    print(a+b)
else:
    print(min(a,b)*2+1)