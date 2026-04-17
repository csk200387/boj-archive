import sys
input = lambda:sys.stdin.readline().rstrip()
arrSize, n = map(int,input().split())
arr = []
for i in range(n) :
	arr.append(input().split())
arr.sort(key=lambda x:int(x[1]))
for i in range(n) :
    if arr[i+1][1] != arr[i][1] :
        print(arr[i+1][0], arr[i+1][1])
        break