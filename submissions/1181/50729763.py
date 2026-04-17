num = int(input())
ar = []
for i in range(num) :
    ar.append(input())

print("\n\n")
for i in sorted(list(set(ar)), key=lambda x:len(x)) :
    print(i)