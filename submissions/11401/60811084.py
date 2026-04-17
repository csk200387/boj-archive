M = 1000000007
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % M
    return result
def power(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n % M
    elif k % 2 == 0:
        y = power(n, k // 2)
        return (y * y) % M
    else:
        return (n * power(n, k - 1)) % M
n, k = map(int, input().split())
N = factorial(n)
K = factorial(n-k) * factorial(k) % M
print(N*power(K, M-2)%M)