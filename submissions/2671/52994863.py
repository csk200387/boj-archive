import re
print("NOISE" if re.fullmatch("(100+1+|01)+",input()) == None else "SUBMARINE")