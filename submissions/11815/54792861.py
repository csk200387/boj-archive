input()
for i in list(map(int, input().split())) :
    if i**0.5 - int(i**0.5) == 0 :
        print(1, end=" ")
    else :
        print(0, end=" ")