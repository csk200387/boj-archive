a,b=map(lambda x:int(x,2),open(0))
mask = 2 ** 100000 - 1
print(f"{bin(a&b)[2:]:0100000b}\n{bin(a|b)[2:]:0100000b}\n{bin(a^b)[2:]:0100000b}\n{bin(ta)[2:]:0100000}\n{bin(tb)[2:]:0100000}")