n = int(input())
arr = list(map(int, input().split()))
start, end = 0, len(arr)-1
am = arr[start] + arr[end]
while start < end:
    s = arr[start] + arr[end]
    if abs(am) > abs(s):
        am = s
        if am == 0:
            break
    if s < 0:
        start += 1
    else:
        end -= 1
print(am)