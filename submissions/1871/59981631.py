t = lambda x:ord(x)-65
for i in range(int(input())) :
    inp = input().split("-")
    sum = t(inp[0][0])*26**2 + t(inp[0][1])*26 + t(inp[0][2])
    if abs(int(inp[1])-sum) <= 100 :
        print("nice")
    else :
        print("not nice")