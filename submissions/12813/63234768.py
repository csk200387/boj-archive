a,b=map(lambda x:int(x,2),open(0))
print(f"{a&b:0100000b}\n{a|b:0100000b}\n{a^b:0100000b}\n{a^1:0100000b}\n{b^1:0100000b}")