import re
c = re.compile("(100+1+|01)+")
i = input()
a = c.match(i)
if a.group() == i :
    print("SUBMARINE")
else :
    print("NOISE")