def sumNum(n) :
    return sum(list(map(int, str(n))))
a = sumNum(input())
stack = 0
while 1 :
    stack += 1
    if len(str(a)) == 1 :
        if a%3 == 0 :
            print(stack, "YES", sep="\n")
            break
        else :
            print(stack, "No", sep="\n")
            break
    else :
        if a%3 == 0 :
            print(stack, "YES", sep="\n")
            break
        else :
            a = sumNum(a)