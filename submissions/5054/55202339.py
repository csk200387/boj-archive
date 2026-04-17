for _ in range(int(input())) :
    input()
    t = sorted(map(int, input().split()))
    print((t[-1]-t[0])*2)