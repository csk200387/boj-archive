a,b=map(lambda x:int(x,2),open(0))
ta = str(bin(int("1"+str(bin(a))[2::].zfill(100000),2)^1))[2::]
tb = str(bin(int("1"+str(bin(b))[2::].zfill(100000),2)^1))[2::]
print(f"{a&b:0100000b}\n{a|b:0100000b}\n{a^b:0100000b}\n{ta:0100000}\n{tb:0100000}")