num = int(input())
for i in range(num) :
    a = input().split()
    n = float(a[0])
    case = a[1::]
    for l in case :
        if l == "@" :
            n *= 3
        elif l == "%" :
            n += 5
        else :
            n -= 7
    print(f"{n:.2f}")