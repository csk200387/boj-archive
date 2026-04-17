n, *arr = open(0)
d,p=0,0
for i in arr :
    if i == "D\n" :
        d += 1
    elif i == "P\n" :
        p += 1
    if abs(p-d) >= 2 :
        print(f"{d}:{p}")
        exit()
print(f"{d}:{p}")