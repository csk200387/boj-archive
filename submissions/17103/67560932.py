import sys
input = lambda:sys.stdin.readline().rstrip()
def eratosthenes(num):
    primes = [True for _ in range(num+1)]
    primes[0] = primes[1] = False
    for i in range(2, num+1):
        if primes[i]:
            for j in range(i*i, num+1, i):
                primes[j] = False
    return primes
def main():
    print_ = print
    data = eratosthenes(1_000_000)
    n = int(input())
    for _ in range(n):
        tmp = int(input())
        cnt = 0
        for i in range(2, tmp//2+1):
            if data[i] and data[tmp-i]:
                cnt += 1
        print_(cnt)

main()