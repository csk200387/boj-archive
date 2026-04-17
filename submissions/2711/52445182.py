for i in range(int(input())) :
    a = input().split()
    b = list(a[1])
    del b[int(a[0])-1]
    print(*b, sep="")