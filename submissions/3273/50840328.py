import sys
input = sys.stdin.readline
a = input()
arr = list(map(int,input().rstrip().split()))
targetNum = int(input().rstrip())
res = 0

for i in range(len(arr)) :
	for l in range(i+1,len(arr)) :
		if arr[i] + arr[l] == targetNum :
			res += 1
print(res)