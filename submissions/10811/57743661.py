N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
for _ in range(M) :
    i, j = map(int, input().split())
    a_arr = arr[:i-1]
    b_arr = list(reversed(arr[i-1:j]))
    c_arr = arr[j:]
    arr = a_arr + b_arr + c_arr
print(*arr)