def mod_factorial(n, m):
    if n >= m:
        return 0
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % m
    return result
n, m = map(int, input().split())
print(mod_factorial(n, m))