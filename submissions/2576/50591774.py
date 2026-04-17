ar = []
for i in range(7) :
    a = int(input())
    if a % 2 != 0 :
        ar.append(a)
print(sum(ar))
print(min(ar))