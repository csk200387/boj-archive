A, B = map(int, input().split())

c = 0
while True:
    if A == B:
        exit(print(c+1))
    if str(B)[-1] == "1":
        if len(str(B)) == 1:
            print(-1)
            exit()
        B = int(str(B)[:-1])
    elif B % 2 == 0:
        B //= 2
    else: 
        exit(print(-1))
    c += 1