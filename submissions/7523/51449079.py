for i in range(int(input())) :
    n, m = map(int,input().split())
    res = ((n+m)*(m-n+1))//2
    print(f"Scenario #{i+1}:\n{res}")