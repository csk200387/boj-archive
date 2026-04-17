for i in input() :
    if ord(i) >= 97 and ord(i) <= 122 :
        asc = ord(i)+13
        if asc <= 97 or asc >= 122 :
            asc -= 26
        print(chr(asc), end="")
    elif ord(i) >= 65 and ord(i) <= 90 :
        asc = ord(i)+13
        if asc <= 65 or asc >= 90 :
            asc -= 26
        print(chr(asc), end="")
    else :
        print(i, end="")