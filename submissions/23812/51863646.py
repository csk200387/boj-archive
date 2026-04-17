n = int(input())
for i in range(5) :
    if i%2 == 0 :
        print(("@"*n + " "*(3*n) + "@"*n+"\n")*n, end="")
    else :
        print(("@"*(5*n)+"\n")*n, end="")