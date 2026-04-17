def eratosthenes(b):
    primes = [True for _ in range(b+1)]
    primes[0] = primes[1] = False
    res = []
    for i in range(2, b+1):
        if primes[i]:
            for j in range(i*i, b+1, i):
                primes[j] = False
    for i in range(b+1):
        if primes[i]:
            res += [i]
    return res
n = int(input())
print(eratosthenes(104742)[n-1])