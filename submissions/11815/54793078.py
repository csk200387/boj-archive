input()
for i in list(map(int, input().split())) :
    if i == int(i**0.5)**2 :
        print(1, end=" ")
    else :
        print(0, end=" ")