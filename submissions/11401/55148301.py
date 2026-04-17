MOD = 1000000007
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % MOD
    return result

def power(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n % MOD
    elif k % 2 == 0:
        y = power(n, k // 2)
        return (y * y) % MOD
    else:
        return (n * power(n, k - 1)) % MOD

n, k = map(int, input().split())
N = factorial(n)
K = factorial(n-k) * factorial(k) % MOD


print(N*power(K, MOD-2)%MOD)