a,b=map(lambda x:int(x,2),open(0))
m = 2 ** 100000 - 1
print(f"{bin(a&b)[2:]:0100000b}\n{bin(a|b)[2:]:0100000b}\n{bin(a^b)[2:]:0100000b}\n{bin(a^m)[2:]:0100000}\n{bin(b^m)[2:]:0100000}")