str = input()
if str.count(str[0]) == len(str) :
    print(-1)
elif str[::-1] == str :
    print(len(str)-1)
else :
    print(len(str))