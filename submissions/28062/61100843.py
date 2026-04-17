n = int(input())
arr = [*map(int, input().split())]
if sum(arr) % 2 == 0:
    print(sum(arr))
else:
    arr.sort()
    for i in arr:
        if i % 2 != 0:
            print(sum(arr) - i)
            break