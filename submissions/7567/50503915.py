g = list(input())
stack = 10
for i in range(1,len(g)):
    if g[i-1] == "(" :
        if g[i] == "(" :
            stack += 5
        else :
            stack += 10
    else :
        if g[i] == ")" :
            stack += 5
        else :
            stack += 10
print(stack)