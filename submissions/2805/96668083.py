n, m = map(int, input().split())
arr = sorted(map(int, input().split()))

start = 0
end = max(arr)
while start <= end:
    mid = (start + end) // 2

    sums = 0
    for i in arr:
        if i > mid: 
            sums += i - mid
    if sums == m:
        print(mid)
        break
    elif sums > m:
        start = mid +1
    else:
        end = mid - 1