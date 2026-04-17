n,*arr = map(int, open(0))
arr.sort(reverse=1)
for i in range(n):
    arr[i] = arr[i]*(i+1)
print(max(arr))