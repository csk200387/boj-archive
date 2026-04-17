ar = []
for _ in range(int(input())) :
    ar.append(int(input()))
ar.sort()
t = []
for i in ar :
    s = 0
    for l in range(i,i+5) :
        if l in ar :
            s += 1
    t.append(s)
print(5-max(t))