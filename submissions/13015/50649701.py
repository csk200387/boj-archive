n = int(input())
for i in range(n) :
    if i == 0 :
        print("*"*n+" "*(n*2-3)+"*"*n)
    elif i == n-1 :
        print(" "*(n-1) + "*" + " "*(n-2) + "*" + " "*(n-2) + "*")
    else :
        print(" "*i + "*" + " "*(n-2) + "*" + " "*((n-i)*2-3) + "*" + " "*(n-2) + "*")
for i in range(n-2,-1,-1) :
    if i == 0 :
        print("*"*n+" "*(n*2-3)+"*"*n)
    else :
        print(" "*i + "*" + " "*(n-2) + "*" + " "*((n-i)*2-3) + "*" + " "*(n-2) + "*")