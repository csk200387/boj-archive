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
    print_ = print
    input_ = input
    while True:
        n = int(input_())
        if n == 0:
            break
        if n % 2 == 1:
            print_("Goldbach's conjecture is wrong.")
            continue

        for i in range(3, n//2+1, 2):
            if i in prime_list and n-i in prime_list:
                print_(f"{n} = {i} + {n-i}")
                break

main()