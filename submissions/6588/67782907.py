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

def main():
    import sys
    input = open("./dev/stdin", "r")
    while True:
        n = int(input.readline())
        if n == 0:
            break
        if n % 2 == 1:
            result += "Goldbach's conjecture is wrong.\n"
            continue

        for i in range(3, n//2+1, 2):
            if i in prime_list and n-i in prime_list:
                result += f"{n} = {i} + {n-i}\n"
                break
    sys.stdout.write(result)
    input.close()
main()