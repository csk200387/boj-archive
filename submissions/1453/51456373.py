n = int(input())
li = list(map(int,input().split()))
ar = [0]*100
stack = 0
for i in li :
	if ar[i-1] == 0 :
		ar[i-1] += 1
	else :
		stack += 1
print(stack)