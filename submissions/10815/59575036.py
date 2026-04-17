a,b,c,d=open(0)
b = map(int,d.split())
d = map(int,b.split())
for i in b :
	if i in d :
		print(1, end=" ")
	else :
		print(0, end=" ")