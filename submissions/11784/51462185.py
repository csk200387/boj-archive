from textwrap import wrap
a = input()
a = wrap(a,2)
for i in a :
    print(chr(int(i, 16)), end="")
    print("")