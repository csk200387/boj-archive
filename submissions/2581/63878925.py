def eratosthenes(a, b):
    primes = [True for _ in range(b+1)]
    primes[0] = primes[1] = False

    for i in range(2, b+1):
        if primes[i]:
            for j in range(i*i, b+1, i):
                primes[j] = False

    res = [i for i in range(a, b+1) if primes[i]]
    return res

a = int(input())
b = int(input())
res = eratosthenes(a,b)

if len(res) == 0 :
    print(-1)
else :
    print(sum(res))
    print(min(res))