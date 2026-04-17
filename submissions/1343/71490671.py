d = input()
arr = []
for i in d.split("."):
    l = len(i)
    if i == '':arr.append(i)
    else:
        if l % 2 == 1:exit(print(-1))
        elif l % 4 == 0:arr.append("A"*l)
        elif l % 2 == 0:
            if l > 2:arr.append("A"*4*(l//4)+"B"*(l%4))
            else:arr.append("B"*l)
print(*arr, sep=".")