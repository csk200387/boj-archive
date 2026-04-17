text = '::1'.split(":")
ar = []
for i in text :
    a = i.zfill(4)
    ar.append(a)
a = ":".join(ar)
if len(ar) < 8 :
    tmp = ":".join(['0000']*(9-len(ar))) 
    print(a.replace("0000",tmp, 1))
else :
    print(a)