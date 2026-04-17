a = 1
b = 123456*2
primes = [True for _ in range(b+1)]
primes[0] = primes[1] = False

for i in range(2, b+1):
    if primes[i]:
        for j in range(i*i, b+1, i):
            primes[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        if primes[i]:
            cnt += 1
    print(cnt)