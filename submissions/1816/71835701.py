def eratosthenes(b):
    primes = [True for _ in range(b+1)]
    primes[0] = primes[1] = False
    for i in range(2, b+1):
        if primes[i]:
            for j in range(i*i, b+1, i):
                primes[j] = False
    return primes
arr = eratosthenes(1000000)
n = int(input())
for _ in range(n):
    num = int(input())
    status = True
    for i in range(2, 1000001):
        if arr[i] and status:
            if num % i == 0:
                status = False
    print("YES" if status else "NO")