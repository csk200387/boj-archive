n = int(input())
ar = []
for i in range(n) :
	a = input()
	if a == "0" :
		try :
			del ar[-1]
		except :
			None
	else :
		ar.append(a)
if len(ar) == 0 :
	print(0)
else :
	print(sum(map(int,ar)))