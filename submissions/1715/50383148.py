import sys
arr = list(map(int,sys.stdin.readline().split()))
for i in range(0,len(arr)):
    arr.insert(2*i+1,arr[i] + arr[i+1])
    arr.sort()
print("+".join(map(str,arr)))