x1, x2 = map(int, input().split())
a, b, c, d, e = map(int, input().split())
sol = lambda X:(1/3)*a*(X**3) + (1/2)*(b-d)*(X**2) + (c-e)*X
print(int(sol(x2)-sol(x1)))