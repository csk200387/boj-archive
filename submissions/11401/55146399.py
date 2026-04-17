MOD = 1000000007
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i % MOD
    return result
def binomial_coefficient(n, k):
    return (factorial(n) * pow(factorial(k) * factorial(n - k), MOD - 2, MOD)) % MOD
n, k = map(int, input().split())
print(binomial_coefficient(n, k))