while True :
    inp = input()
    if inp == "0" :
        break
    else :
        inp = inp.split()[1::]
        tmp = []
        for i in inp :
            if i in tmp :
                pass
            else :
                tmp.append(i)
        tmp.append('$')
        print(" ".join(tmp))