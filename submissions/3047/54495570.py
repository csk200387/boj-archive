arr = list(map(int, input().split()))
for i in sorted(input(), reverse=True) :
    print(arr[67-ord(i)], end=" ")