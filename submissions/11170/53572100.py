for _ in range(int(input())) :
    n, m = map(int, input().split())
    arr = [str(i) for i in range(n,m+1)]
    print(("".join(arr)).count("0"))