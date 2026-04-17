import math
n, k = map(int,input().split())
n_fac = math.factorial(n)%1000000007
k_fac = math.factorial(k)%1000000007
nk_fac = math.factorial(n-k)%1000000007
print(int(n_fac / (k_fac*nk_fac))%1000000007)