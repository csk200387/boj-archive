import sys
sys.setrecursionlimit(2000)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) % 1_000_000_007

n, k = map(int, sys.stdin.readline().strip().split())

print(int(factorial(n) / (factorial(k) * factorial(n-k))))