CYCLE = 374995999999
def fibonacci(n):
    a, b = 0, 1
    cnt = 0
    for i in range((n-1) % 1500000):
        a, b = b, (a + b) % 1_000_000
        if i % 2 == 0:
            cnt += b
    return cnt
n = int(input())
C = n // 1500000
N = n % 1500000
print((C*CYCLE+fibonacci(n))%1_000_000_007)