n = int(input())
arr = [i+1 for i in range(n)]
while len(arr) != 1:
    arr.pop(0)
    arr.append(arr.pop(0))
print(arr[0]+1)