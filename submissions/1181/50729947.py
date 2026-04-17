num = int(input())
ar = []
for i in range(num) :
    ar.append(input())
for i in sorted(list(set(ar)), key=lambda x:(len(x), x[0])) :
    print(i)