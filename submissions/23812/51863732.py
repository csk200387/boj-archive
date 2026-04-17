n = int(input())
for i in range(5) :
    print(("@"*n + " "*(3*n) + "@"*n+"\n")*n if i%2 == 0 else ("@"*(5*n)+"\n")*n, end="")