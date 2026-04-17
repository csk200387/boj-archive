import re
c = re.compile("(100+1+|01)+")
i = input()
a = c.fullmatch(i)
if a == None :
    print("NOISE")
else :
    print("SUBMARINE")