ar = []
for _ in range(3) :
    ar.append(int(input()))
if sum(ar) != 180 :
    print("Error")
else :
    if ar[0] == ar[1] and ar[1] == ar[2] :
        print("Equilateral")
    elif ar[0] == ar[1] or ar[1] == ar[2] or ar[2] == ar[0] :
        print("Isosceles")
    else :
        print("Scalene")