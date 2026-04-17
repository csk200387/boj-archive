a, b = map(int, input().split())
arr = [[] for i in range(a)]
arr[0] = [1]
for i in range(1, a):
    for l in range(i+1):
        if l == i or l == 0:
            arr[i].append(1)
        else:
            arr[i].append(arr[i-1][l]+arr[i-1][l-1])
print(arr[a-1][b-1])