input()
arr = list(map(int, input().split()))
t = 0
for i in range(max(arr)):
    tmp = arr.count(i+1)
    if tmp > t:
        t = tmp
print(t)