N, M = map(int, input().split())
arr = [[0]*N for _ in range(N)]
for i in range(M) :
    i, j, k = map(int, input().split())
    for l in range(i-1, j) :
        arr[l].append(k)
for i in range(N) :
    print(arr[i][-1], end=" ")