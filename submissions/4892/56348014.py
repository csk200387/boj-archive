stack = 1
while True :
    n0 = int(input())
    if n0 == 0 :
        break
    else :
        n1 = n0*3
        if n1 & 1 == 0 :
            n2 = n1/2
            res = "even"
        else :
            n2 = (n1+1)/2
            res = "odd"
        n3 = n2*3
        n4 = int(n3//9)
        print(f"{stack}. {res} {n4}")
        stack += 1