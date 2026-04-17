a = int(input())
i = 1
while True:
    if a == i+sum(map(int,list(str(i)))) :
        print(i)
        break
    else :
        i += 1
        if i > a :
            print(0);
            break