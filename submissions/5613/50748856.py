res = int(input())
while True :
    a = input()
    if a == "=" :
        break
    else :
        b = int(input())
        if a == "+" :
            res += b
        elif a == "-" :
            res -= b
        elif a == "*" :
            res *= b
        elif a == "/" :
            res /= b
            res = int(res)
print(res)