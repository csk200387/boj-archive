for i in range(int(input())):
    a=input().split()
    r=[]
    for i in range(len(a[1])):
        r.append(a[1][i]*int(a[0]))
    print(*r,sep="")