ans = input()
E, S, M = 1, 1, 1
stack = 1
while True :
	if ans == f"{E} {S} {M}" :
		print(stack)
		break
	else :
		stack += 1
		E += 1
		S += 1
		M += 1
		if E > 15 :
			E = 1
		if S > 28 :
			S = 1
		if M > 19 :
			M = 1