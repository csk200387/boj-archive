tmp = ""
str = input()
if str.count(str[0]) == len(str) :
    print(-1)
elif str != str[::-1] :
    print(len(str))
else :
    for i in range(len(str)) :
        if str[i::-1] == str :
            print(len(tmp))
            break
        else :
            tmp = str[i::-1]