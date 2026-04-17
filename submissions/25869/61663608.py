a, b, c = map(int, input().split())
t = (a-c*2) * (b-c*2)
print(t if t >= 0 else 0)