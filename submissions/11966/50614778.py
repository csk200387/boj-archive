a = int(input())
ar = []
for i in range(40) :
    ar.append(2**i)

if a in ar :
    print(1)
else :
    print(0)