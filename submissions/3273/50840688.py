import sys
input = sys.stdin.readline
a = input()
arr = list(map(int,input().rstrip().split()))
targetNum = int(input().rstrip())
res = 0
arr.sort()
for i in range(len(arr)) :
	for l in range(len(arr)-1,i-1,-1) :
		if arr[i] + arr[l] == targetNum :
			res += 1
print(res)