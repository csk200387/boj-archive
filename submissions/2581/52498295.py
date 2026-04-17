m = int(input())
n = int(input())

# 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
is_prime = [True] * (n+1)

# n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * 2, n, i):
            is_prime[j] = False

# 소수 목록 산출
primes = []
for i in range(2, n+1):
    if is_prime[i]:
        primes.append(i)

# m이상 n이하의 소수만 추출
selected_primes = []
for prime in primes:
    if prime < m:
        continue
    if prime > n:
        break
    selected_primes.append(prime)

# 추출한 소수의 합과 최솟값 출력
if selected_primes:
    print(sum(selected_primes))
    print(min(selected_primes))
else:
    print(-1)