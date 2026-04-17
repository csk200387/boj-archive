data =  input()

res = []
a, b = 0, 0
wa, wb = 0, 0
for i in data:
    if i == "A":
        a += 1
    else:
        b += 1
    
    if a == 21:
        wa += 1
        res.append(f"{a}-{b}")
        a, b = 0, 0
    elif b == 21:
        wb += 1
        res.append(f"{a}-{b}")
        a, b = 0, 0

print(*res, sep="\n")
print("A" if wa > wb else "B")