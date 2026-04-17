n = int(input())
arr = list(map(int, input().split()))
m = int(input())
start = 1
end = max(arr)
while start <= end:
    mid = (start + end) // 2
    sums = 0
    for i in arr:
        if i > mid:
            sums += mid
        else:
            sums += i
    if sums <= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)