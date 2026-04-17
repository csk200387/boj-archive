while True :
    inp = input()
    if inp == "0" :
        break
    else :
        ar = inp.split()
        tmp = [ar[1]]
        inp = ar[1::]
        for i in range(1,len(inp)) :
            if tmp[-1] == inp[i] :
                pass
            else :
                tmp.append(inp[i])
        tmp.append('$')
        print(" ".join(tmp))