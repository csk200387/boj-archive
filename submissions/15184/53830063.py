l = input().upper()
for i in range(26) :
    c = chr(65+i)
    s = "*"*l.count(c)
    print(f"{c} | {s}")