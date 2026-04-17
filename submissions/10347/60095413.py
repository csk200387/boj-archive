t="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."*2
while 1:
    i=input()
    if i=='0':
        exit()
    a,b = i.split()
    for j in range(len(b)-1,-1,-1):
        print(t[t.index(b[j])+int(a)],end="")
    print()