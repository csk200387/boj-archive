def convert_notation(n, base):
    T = "0123456789abcdef"
    q, r = divmod(n, base)

    return convert_notation(q, base) + T[r] if q else T[r]

for i in range(1000,10000) :
	t = i
	tw = convert_notation(i, 12)
	he = hex(i)[2:]
	t_arr = []
	tw_arr = []
	he_arr = []
	for l in str(t) :
		t_arr.append(int(l))
	for l in tw :
		tw_arr.append(int(l.replace("a","10").replace("b","11").replace("c","12").replace("d","13").replace("e","14").replace("f","15")))
	for l in he :
		he_arr.append(int(l.replace("a","10").replace("b","11").replace("c","12").replace("d","13").replace("e","14").replace("f","15")))
	if sum(t_arr) == sum(tw_arr) == sum(he_arr) :
		print(i)