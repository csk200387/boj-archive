N, M = map(int, input().split())
arr = [*range(1,N+1)]
for _ in range(M) :
    a, b, c = map(int, input().split())
    arr = arr[:a-1] + arr[c-1:b] + arr[a-1:c-1] + arr[b:]
print(*arr)