a,b=map(lambda x:int(x,2),open(0))
n = 100000
m = 2 ** n - 1,
print(bin(a&b)[2:].zfill(n))
print(bin(a|b)[2:].zfill(n))
print(bin(a^b)[2:].zfill(n))
print(bin(a^m)[2:].zfill(n))
print(bin(b^m)[2:].zfill(n))