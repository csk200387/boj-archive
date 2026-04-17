l, r, n = map(int, [i.strip() for i in open(0)])
count = (r//n) - ((l-1)//n)
print(count * (count-1) // 2)
