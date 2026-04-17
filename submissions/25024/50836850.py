import sys
input = sys.stdin.readline

a = int(input().rstrip())
for i in range(a) :
	a = list(map(int,input().rstrip().split()))
	x = a[0]
	y = a[1]
	if x < 24 and y < 60 :
		print("Yes", end=" ")
	else :
		print("No", end=" ")
	if x < 13 :
		if x in [1,3,5,7,8,10,12] and y < 32 :
			print("Yes")
		elif x in [4,6,9,11] and y < 31 :
			print("Yes")
		elif x == 2 and y < 30 :
			print("Yes")
		else :
			print("No")
	else :
		print("No")