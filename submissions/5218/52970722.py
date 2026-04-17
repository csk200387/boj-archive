for i in range(int(input())) :
    a, b = input().split()
    print("Distances:", end="")
    for i in range(len(a)) :
        t1 = ord(b[i])-ord(a[i])
        print("", t1 if t1 >= 0 else t1+26, end="")
    print()