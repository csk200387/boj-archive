n, mod = map(int, input().split())
arr = list(map(int, input().split()))
result = 1
for i in range(n):
    result *= (arr[i] % mod)
print(result % mod)