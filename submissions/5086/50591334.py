while True :
    a = list(map(int,input().split()))
    if a[0] == 0 and a[1] == 0 :
        break
    elif a[0] // a[1] == 0 :
        print("factor")
    elif a[0] % a[1] == 0 :
        print("multiple")
    else :
        print("neither")