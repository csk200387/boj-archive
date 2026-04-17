arr = list(map(int, input().split()))
for i in sorted(input()) :
    print(arr[65-ord(i)], end=" ")