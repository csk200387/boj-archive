ar = []
for i in range(7) :
    a = int(input())
    if a % 2 != 0 :
        ar.append(a)
if len(ar) == 0 :
    print(-1)
else :
    print(sum(ar))
    print(min(ar))