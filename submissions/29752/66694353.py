size = int(input())
arr = list(map(int, input().split()))
try:
    t = arr.index(0)
    print(t)
except ValueError:
    print(len(arr))