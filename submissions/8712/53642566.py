n = int(input())
for i in range(n) :
    if i%2 == 0 :
        print(*range(n*i+1, n*(i+1)+1), sep=" ") 
    else :
        print(*range(n*(i+1), n*i, -1), sep=" ")