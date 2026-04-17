a,b,c,d=open(0)
for i in map(int,d.split()) :
	if i in map(int,b.split()) :
		print(1, end=" ")
	else :
		print(0, end=" ")