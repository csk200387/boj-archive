num = int(input())
inp = list(map(int,input().split()))
arr = []
stack = 1
for i in inp :
	if i == inp[0] :
		arr.append(i)
	else :
		if arr[-1] <= i :
			print(i)
			arr.append(i)
			stack += 1
print(stack)