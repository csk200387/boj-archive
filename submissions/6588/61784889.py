def sieve_of_eratosthenes(n):
    sieve = [False, False] + [True] * (n - 1)
    p = 2
    while p * p <= n:
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1
    primes = [i for i in range(2, n + 1) if sieve[i]]
    return primes

def binary_search(arr, x):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1 

prime_list = sieve_of_eratosthenes(1000000)
while True:
    n = int(input())
    if n == 0:
        break
    if n % 2 == 1:
        print("Goldbach's conjecture is wrong.")
        continue

    for i in range(len(prime_list)):
        if binary_search(prime_list, n-prime_list[i]) != -1:
            print(f"{n} = {prime_list[i]} + {n-prime_list[i]}")
            break