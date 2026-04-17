for i in range(int(input())) :
    data = input().strip()
    if data.isdigit() :
        print(int(data))
    else :
        print("invalid input")