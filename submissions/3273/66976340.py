n = int(input())
arr = list(map(int, input().split()))
s = int(input())
arr.sort()

l, r = 0, n-1
res = 0

while l < r:
    tmp = arr[l] + arr[r]
    if tmp == s:
        res += 1
        l += 1
        r -= 1
    elif tmp < s:
        l += 1
    else:
        r -= 1

print(res)