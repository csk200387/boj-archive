n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
start = 1
end = max(arr)
while start <= end:
    mid = (start + end) // 2

    sums = 0
    for i in arr:
        if i >= mid: 
            sums += i - mid
    if sums >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)