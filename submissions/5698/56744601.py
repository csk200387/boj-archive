while True :
    line = input()
    if line == "*" :
        break
    else :
        arr = [i[0].lower() for i in line.split()]
        if len(set(arr)) == 1 :
            print("Y")
        else :
            print("N")