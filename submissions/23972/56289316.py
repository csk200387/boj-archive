import math
K, N = map(int, input().split())
if N == 1 :
    print(-1)
else :
    res = math.ceil(N*K//(N-1))
    print(res)