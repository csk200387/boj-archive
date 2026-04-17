t="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."*2
while 1:
    i=input()
    if i=='0':
        exit()
    a,b = i.split()
    print(*[t[t.index(i)+int(a)] for i in b[::-1]],sep="")