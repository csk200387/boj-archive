def eratosthenes(n):
    primes = [True for _ in range(104743)]
    primes[0] = primes[1] = False
    res = 0
    count = 0
    for i in range(2, 104743):
        if primes[i]:
            for j in range(i*i, 104743, i):
                primes[j] = False
    for i in range(104743):
        if primes[i]:
            res = i
            count += 1
            if count == n:
                break
    return res
print(eratosthenes(int(input())))