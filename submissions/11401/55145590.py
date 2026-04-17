import sys
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i % 1_000_000_007
    return result

n, k = map(int, sys.stdin.readline().strip().split())

print(int(factorial(n) / (factorial(k) * factorial(n-k))))