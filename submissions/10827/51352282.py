inp = input().split()
a = inp[0]
b = int(inp[1])
tmp = int(str(a).replace(".",""))
a1 = str(tmp**b)
result = str(float(a)**b).split('.')[0]
print(result+'.'+a1[len(result)::])