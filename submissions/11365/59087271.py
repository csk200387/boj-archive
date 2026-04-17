for i in open(0):
    if i == "END\n" :
        break
    else :
        print(i[::-1], end="")