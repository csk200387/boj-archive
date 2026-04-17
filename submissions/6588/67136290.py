import sys
input = lambda:sys.stdin.readline().rstrip()


def sieve_of_eratosthenes(n):
    sieve = [False, False] + [True] * (n - 1)
    p = 2
    while p * p <= n:
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1
    primes = {i for i in range(2, n + 1) if sieve[i]}
    return primes

prime_list = sieve_of_eratosthenes(1000000)
while True:
    n = int(input())
    if n == 0:
        break
    if n % 2 == 1:
        sys.stdout.write("Goldbach's conjecture is wrong.\n")
        continue

    for i in range(3, n//2+1, 2):
        if i in prime_list and n-i in prime_list:
            sys.stdout.write(f"{n} = {i} + {n-i}\n")
            break