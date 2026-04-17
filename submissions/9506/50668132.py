while True :
    a = []
    inp = int(input())
    if inp == -1 :
        break
    else :
        for i in range(1,inp) :
            if inp % i == 0 :
                a.append(i)
        if inp == sum(a) :
            b = " + ".join(list(map(str,a)))
            print(f"{inp} = {b}")
        else :
            print(f"{inp} is NOT perfect.")