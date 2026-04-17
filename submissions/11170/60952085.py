for _ in range(int(input())) :
    t = 0
    n, m = map(int, input().split())
    for i in range(n,m+1) :
        t += str(i).count("0")
    print(t)