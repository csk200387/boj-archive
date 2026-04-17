num = input("").split(" ")
    A = int(num[0])
    B = int(num[1])
    C = B - 45

    if(C < 0):
        A -= 1
        if(A < 0):
            A = 23
        C = 60 + C
    print(A,B)