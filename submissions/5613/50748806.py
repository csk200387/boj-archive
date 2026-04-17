res = int(input())
while True :
    a = input()
    if a == "=" :
        break
    else :
        if a == "+" :
            b = int(input())
            res += b
            continue
        elif a == "-" :
            b = int(input())
            res -= b
            continue
        elif a == "*" :
            b = int(input())
            res *= b
            continue
        elif a == "/" :
            b = int(input())
            res /= b
            res = int(res)
            continue
print(res)