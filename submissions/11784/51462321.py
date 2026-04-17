from textwrap import wrap
while 1:
    try:
        a = input()
        a = wrap(a,2)
        for i in a :
            print(chr(int(i, 16)), end="")
        print("")
    except EOFError:
        break