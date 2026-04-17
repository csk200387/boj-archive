for _ in range(int(input())) :
    n = 0
    n, m = map(int, input().split())
    for i in range(n,m+1) :
        n += str(i).count("0")
    print(n)