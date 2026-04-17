ar = input().split()
score = input()
a = ar.index(score)
if a < 5 :
	print("A+")
elif a < 15 :
	print("A0")
elif a < 30 :
	print("B+")
elif a < 35 :
	print("B0")
elif a < 45 :
	print("C+")
elif a < 48 :
	print("C0")
else :
	print("F")