for _ in range(int(input())):
    i,a,b,c,d = map(float, input().split())
    print(f"{i:.0f} {(a*d)/(b+c):.2f}")