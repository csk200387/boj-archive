while True:
    try:
        data = input()
        if data == '#':
            exit()
        data = data.split()
        print(*data, end=" ")
        for i in range(len(data[0])):
            txt = chr(ord(data[2][i])+ord(data[1][i]) - ord(data[0][i]))
            if 97 <= ord(txt) <= 122:
                print(txt, end='')
            elif ord(txt) < 97:
                print(chr(ord(txt)+26), end='')
            else:
                print(chr(ord(txt)-26), end='')
        print()
    except:
        break