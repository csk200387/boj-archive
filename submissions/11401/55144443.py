def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) % 1_000_000_007

n, k = map(int, input().split())

print(int(factorial(n) / (factorial(k) * factorial(n-k))))