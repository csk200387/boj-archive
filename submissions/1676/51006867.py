A = int(input())
stack = 0
sum = 1
for i in range(1,A+1) :
	sum *= i
for i in str(sum)[::-1] :
	if i != "0" :
		print(stack)
		break
	stack += 1